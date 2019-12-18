#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler

allowed_domains = {
    "domain1.com": "Hello Domain1",
    "domain2.com": "Hello Domain2"
}


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.route()

    def route(self):
        if self.is_domain_allowed():
            content = self.get_domain_content()
            body = '<html><body><p>{}</p></body></html>'.format(content).encode('utf-8')

            self.send_response(200, 'OK')
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', len(body))
            self.send_header('Server', 'demo')
            self.end_headers()
            self.wfile.write(body)
        else:
            # TODO: what happens if the domain is not allowed / Host header incorrect
            raise Exception("Not implemented yet")

    def is_domain_allowed(self):
        # TODO: read Host header and match the domain
        # Use: self.headers array to get header's value
        # https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.headers

        return True

    def get_domain_content(self):
        # TODO: read Host header and get the content
        return ""


server = HTTPServer(('', 8080), RequestHandler)

if __name__ == "__main__":
    print('Listening on port 8080')
    server.serve_forever()
