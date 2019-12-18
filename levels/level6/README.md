# Level 6: Going low level
In this exersice we will explore the internals of an HTTP server and work with sockets directly. You mission, if you choose to accept it, is to parse the request properly and build a functioning HTTP server returning `200 OK` to a simple request

## Questions
- Why are we using a buffer to read the request line and headers separate from the body?
- What size would give the headers buffer? why?
- Try sending your server a body with the wrong size (different from `Content-Length`)


## Documentation
- [Python socket module](https://docs.python.org/3.7/library/socket.html)