# Level 8: Keep-Alive (i.e. Connection Reuse)
HTTP/1.1 allows us to keep a connection (socket) open for more incoming requests to be served re-using the original TCP socket.
In this exercise, we going to implement connection re-use in our low-level code.  

Connection re-using is based on two headers:
- `Connection` header which allow us to control whether the connection should be open after the transcation or not.
- `Keep-Alive` header which specifies how the keep-alive should behave

We'll need to read the `Connection` header, and behave according to the request value:
- If request is sent with `Connection` header and the value is 'keep-alive', then preserve the connection open for next incoming requests.
- If another request is sent with `Connection` header and the value is 'close', close the kept connection.

Note that since we implement a single threaded web server, new connections won't be able to process until the original connection is closed.

## Exercise
- Implement the keep-alive behavior in the low-level server.py (search for TODO)

## Questions
- Does the browser sends `Connection` close header? How can we close the connection?

## Documentation
- [Python socket module](https://docs.python.org/3.7/library/socket.html)
- [Python time module](https://docs.python.org/3.7/library/time.html)