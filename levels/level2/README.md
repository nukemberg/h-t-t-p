# Level 2: Fun with redirects
Implement a redirect response on `/redirect` by returning a 30x redirect status code with a proper `Location` header.

## Exercises
- Create a redirect loop and see how the browser responds to it
- Try different redirect codes: 301, 302, 303, 307, 308; try changing the redirect URLs (perhaps using `random.choice()`?), which codes are cached?
- Try redirecting to a non-URL string

## References
- [Location on MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Location)
- [Redirections on MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections)
- [Python HTTPServer docs](https://docs.python.org/3.7/library/http.server.html)