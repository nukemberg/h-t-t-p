# Level 4: Caching
For proper caching, the server needs to tell the client (or proxies along the way) if and how to cache the payload. This means we need to send the proper caching headers:
- `Cache-Control` - various directives controling cache behavior. See the docs for more info
- `ETag` - a hash of the content
- `Expires` - the date/time after which the response is considered stale
- `Last-Modified` - the time when the body (content) was generated
- `Vary` - Controls the cache subkey to allow caching of multiple variant of the same page (e.g. languages, user-agent)

## Exercises
- Can you use a cached page offline? turn the server off and check if the browser can still use the page
- What is the difference between `no-store` and `no-cache` directives of the `Cache-Control` header?
- How do you tell proxies _not_ to cache a response?
- Bonus: implement support for conditional GET response and `304 NOT MODIFIED` response

# Documentation
- [`Last-Modified` on MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Last-Modified)
- [`Expires` on MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expires)
- [`Cache-Control` on MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control)
- [`ETag` on MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag)