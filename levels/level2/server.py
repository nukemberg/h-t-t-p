#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # TODO: redirect the browser to the DevOpsDays TLV website (https://devopsdays.org/events/2019-tel-aviv/welcome/)
        if self.path == '/redirect':
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

