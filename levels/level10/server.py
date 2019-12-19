#!/usr/bin/env python3

import time
from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Javascript client side code opens EventSource on the browser
        body = """<html><body><h1>Streaming baby!</h1>
        <ul id="events">
        </ul>
<script>
const eventSource = new EventSource("/sse")
eventSource.onmessage = function(event) {
    const list = document.querySelector("ul#events")
    const elmnt = document.createElement("li")
    elmnt.innerText = "data: " + event.data
    list.appendChild(elmnt)
}
</script>
</body></html>""".encode('utf-8')
        if self.path == '/':
            self.send_response(200, 'OK')
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(body)
            self.wfile.flush()
        elif self.path == '/sse':
            # TODO: Implement SSE
            while True:
                # TODO: send frames every 3 seconds, don't forget to flush!
                time.sleep(3)

        else:
            self.send_response(404, 'Not found')
            # after sending the status line, we send headers
            self.send_header('Server', 'demo')
            self.end_headers()
        

server = HTTPServer(('', 8080), RequestHandler)

if __name__ == "__main__":
    print('Listening on port 8080')
    server.serve_forever()

