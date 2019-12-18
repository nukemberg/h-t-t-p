# Level 6: Going low level
In this exersice we will explore the internals of an HTTP server and work with sockets directly. You mission, if you choose to accept it, is to parse the request properly and build a functioning HTTP server returning `200 OK` to a simple request

## Questions
- Why are we using a buffer to read the request line and headers and not reading line by line (or byte by byte)?
- What size would give the headers buffer? why?
- What would happen if a client sent a header line with infinite length?

## Documentation
- [Python socket module](https://docs.python.org/3.7/library/socket.html)