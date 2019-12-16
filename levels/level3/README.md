# Level 3: Body movin'
Modify the server to send a `200 OK` response along with body and relevant content headers:
- `Content-Type` should be set to `text/html` with appropriate charset
- `Content-Length` should be set to the size of the body in bytes
After writing the headers, send the body using the `self.wfile.write()` function.

## Exercises
- What happens when you send a body with the wrong content-length? smaller? larger?
- What happens when you send the wrong encoding? e.g. body is encoded in python as UTF-8 but `Content-Type` specifies `iso-8859-1` encoding? try this emoji 😁

## References
- [Content-Length on MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Length)
- [Content-Type on MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)
- [Python HTTPServer docs](https://docs.python.org/3.7/library/http.server.html)