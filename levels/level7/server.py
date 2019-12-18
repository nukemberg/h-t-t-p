import socket
import json
from io import BytesIO
import logging
import sys
from http import HTTPStatus

DEFAULT_RESPONSE_HEADERS = (
    ('Content-Type', 'text/html; charset=utf-8'),
    ('Server', 'H-T-T-P')
)

_MAXLINE = 65536
_MAXHEADERS = 100
HEADERS_BUFFER_SIZE = 64*1024  # 64kb
BODY_BUFFER_SIZE = 8*2**20 # 8MB
HTTP_METHODS = (
    b'OPTIONS',
    b'GET',
    b'POST',
    b'PUT',
    b'DELETE',
    b'TRACE',
    b'CONNECT'
)

def _to_bytes(x):
    if type(x) == bytes:
        return x
    elif type(x) == str:
        return x.encode()
    else:
        return str(x).encode()

class MalformedRequestError(Exception):
    pass

class UnsupportedMethodError(Exception):
    pass

def find_header(headers, name):
    try:
        return tuple(s.lower() for s in next(filter(lambda header: header[0].lower() == name.lower(), headers)))
    except StopIteration:
        return None


def parse_content_length(headers):
    header = find_header(headers, 'content-length')
    try:
        return int(header)
    except (ValueError, TypeError):
        return None


def method_has_body(method):
    return method in ('POST', 'PUT')


def parse_header_line(line):
    key, value = line.split(b':', 1)
    return key.decode('ISO-8859-1').strip(), value.decode('ISO-8859-1').strip()


def parse_headers(_reader):
    headers = []
    while True:
        line = _reader.readline()
        if len(line) > _MAXLINE:
            raise MalformedRequestError('Header line too long')

        if line in (b'\r\n', b'\n', b''):
            break

        headers.append(parse_header_line(line))

        if len(headers) > _MAXHEADERS:
            raise Exception('got more than {} headers'.format(_MAXHEADERS))

    return headers


def parse_request_line(_reader):
    line = _reader.readline()
    if line == b'':  # nothing read from socket, it's probably closed
        raise ConnectionAbortedError
    parts = line.split()
    if len(parts) != 3:
        logging.debug('request: {}'.format(line))
        raise MalformedRequestError('Request line malformed')
    return parts


def parse_request(_socket):
    buff = BytesIO(_socket.recv(HEADERS_BUFFER_SIZE))
    (method, path, protocol) = parse_request_line(buff)
    if method not in HTTP_METHODS:
        raise UnsupportedMethodError('Method not supported')
    headers = parse_headers(buff)
 
    # presumably anything left in the headers buffer reader is part of the body so we concatenate
    # if we just recv() more from the socket we might block, perhaps there isn't more to read?
    # How do we know if a socket is closed?
    body_start = buff.read()
    body = None

    # TODO: read the rest of the body from the socket, concatenate it with body_start
    # Don't forget Content-Length
        
    return {
        'headers': headers,
        'method': method,
        'path': path,
        'protocol': protocol,
        'body': body
    }


def _to_bytes(x):
    if type(x) == bytes:
        return x
    elif type(x) == str:
        return x.encode()
    else:
        return str(x).encode()


def respond(conn, protocol, status_code, status_text, headers, body=None):
    conn.sendall(b' '.join(_to_bytes(x) for x in (protocol, status_code, status_text)) + b'\r\n')
    for header in headers:
        conn.sendall((_to_bytes(header[0]) + b': ' + _to_bytes(header[1]) + b'\r\n'))
    conn.sendall(b'\r\n')
    if body:
        conn.sendall(body)


def handle_request(conn):
    req = parse_request(conn)
    respond(conn, req['protocol'], 200, 'OK', DEFAULT_RESPONSE_HEADERS + (('Content-Length', '0'),), '')
    return req


def handle_connection(conn):
    try:
        req = handle_request(conn)
    except MalformedRequestError:
        respond(conn, 'HTTP/1.1', HTTPStatus.BAD_REQUEST.value, 'Bad request', DEFAULT_RESPONSE_HEADERS)
    except UnsupportedMethodError:
        respond(conn, 'HTTP/1.1', HTTPStatus.METHOD_NOT_ALLOWED.value, 'Method not allowed', DEFAULT_RESPONSE_HEADERS)
    except ConnectionAbortedError:
        logging.info('Connection aborted')
    except Exception as e:
        logging.warn('Exception while handling request', exc_info=e)
    conn.close()


def init(port):
    logging.basicConfig(level=logging.INFO)

    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _socket.bind(('', port))
    _socket.listen()
    logging.info('listening on port {}'.format(port))

    while True:
        conn, addr = _socket.accept()
        logging.info('New connection from {}'.format(addr)) 
        handle_connection(conn)


if __name__ == "__main__":
    init(8080)

