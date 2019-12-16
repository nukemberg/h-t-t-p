#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # TODO: return status code 200 OK
            pass
        else:
            self.send_response(404, 'Not found')
            
        # after sending the status line, we send headers
        self.send_header('Server', 'demo')
        self.end_headers()
        

server = HTTPServer(('', 8080), RequestHandler)

if __name__ == "__main__":
    print('Listening on port 8080')
    server.serve_forever()

