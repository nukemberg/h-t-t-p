# Level 5: Virtualhosting
One of the great improvements of HTTP/1.1 is the `Host` header.
Using this header we can preserve the original domain the request was sent to, and in this exercise
we'll leverage that header in order to implement [VirtualHosting](https://en.wikipedia.org/wiki/Virtual_hosting)

You'll need to implement function `is_domain_allowed` and `get_domain_content` to return different responses according to the domain:  
```
domain1.com => "Hello Domain1"  
domain2.com => "Hello Domain2"
```

## Exercises
- Return HTML response only for set of allowed domains like in the example above
- Does the `Host` header contains the server port? How we can deal that?
- What happens if the request doesn't contains `Host` header? (Hint: [Bad Request](https://tools.ietf.org/html/rfc2616#section-14.23))
- What happens if a request was sent with `Host` header contains unsupported domain? (Hint: [Bad Request](https://tools.ietf.org/html/rfc2616#section-5.2))
- Bonus: how we can check it locally and simulating requests to `domain1.com` and `domain2.com` without owning the domains?

# Documentation
- [`Host` on MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Host)
- [`headers` of Python BaseHTTPRequestHandler](https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.headers)