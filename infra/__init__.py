from io import BytesIO
from logging import Logger
_MAXLINE = 65536
_MAXHEADERS = 100
HEADERS_BUFFER_SIZE = 64*1024  # 64kb
BODY_BUFFER_SIZE = 8*2**20 # 8MB
HTTP_METHODS = (
    'OPTIONS',
    'GET',
    'POST',
    'PUT',
    'DELETE',
    'TRACE',
    'CONNECT'
)

logger = Logger('infra')

class MalformedRequestError(Exception):
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
            raise Exception('Header line too long')

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
        logger.debug('request: {}'.format(line))
        raise Exception('Request line malformed')
    return parts


def parse_request(_socket):
    buff = BytesIO(_socket.recv(HEADERS_BUFFER_SIZE))
    (method, path, protocol) = parse_request_line(buff)
    headers = parse_headers(buff)
    connection_header = find_header(headers, 'connection')
    if connection_header and connection_header[1] == 'keep-alive' and protocol == 'HTTP/1.1':
        close = True
    else:
        close = False

    # presumably anything left in the headers buffer reader is part of the body so we concatenate
    body_start = buff.read()
    # if we just recv() more from the socket we might block, perhaps there isn't more to read?
    content_length = parse_content_length(headers)
    if method_has_body(method) and content_length > 0:
        body_rest = _socket.recv(content_length)
        body = BytesIO(body_start + body_rest)
    else:
        body = BytesIO(body_start)
        
    return {
        'headers': headers,
        'method': method,
        'path': path,
        'protocol': protocol,
        'body': body,
        'close': close
    }
