import socket
from infra import parse_request, method_has_body, find_header
import json
from io import BytesIO
import logging
import sys

DEFAULT_RESPONSE_HEADERS = (
    ('Content-Type', 'text/html; charset=utf-8'),
    ('Server', 'H-T-T-P')
)


def _to_bytes(x):
    if type(x) == bytes:
        return x
    elif type(x) == str:
        return x.encode()
    else:
        return str(x).encode()


def respond(conn, protocol, status_code, status_text, headers, body):        
    conn.sendall(b' '.join(_to_bytes(x) for x in (protocol, status_code, status_text)) + b'\r\n')
    for header in headers:
        conn.sendall((_to_bytes(header[0]) + b': ' + _to_bytes(header[1]) + b'\r\n'))
    conn.sendall(b'\r\n')


def handle_request(conn):
    req = parse_request(conn)
    respond(conn, req['protocol'], 200, 'OK', DEFAULT_RESPONSE_HEADERS + (('Content-Length', '0'),), '')
    return req


def handle_connection(conn):
    try:
        req = handle_request(conn)
        while not req['close']:
            logging.info('Reusing connection')
            req = handle_request(conn)
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


init(8080)