# Level 7: Body movin' (breakdance version)
In the previous exercise we made our server handle a simple bodyless request. We will now add support for reading the body from requests.

## Questions
- Why are we using a buffer to read the request line and headers separate from the body?
- What size would give the headers buffer? why?
- Try sending your server a body with the wrong size (different from `Content-Length`). What is the correct behavior in this case? why?
- What happens if a client sends an inifinite stream of bytes as the body?
- Bonus: add gzip support using the [python gzip module](https://docs.python.org/3.7/library/gzip.html) and the [`Content-Encoding`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding) header

## Documentation
- [`Content-Length` on MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Length)
