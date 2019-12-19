# Level 9: Timeout
Until now, we implemented mostly naive HTTP server that handles simple request-response flows.
In the real life, we have dozes of clients behaving completely differently and since we're trying to write
serious server we need to protect ourselves. One of the most important concepts we have in web server are timeouts.

There's a few different types of timeouts, such as the following:
- Connection timeout (how long it takes to connect to server by a client)
- Read timeout (how long it takes to read bytes from socket, both for client and server)
- Idle timeout (how long we allow a connection to stay open without activity, for example in keep-alive case)
- Processing timeout (how long we allow the *server* to work on specific request)

In this exercise, we'll implement request (read) timeout.  
If it takes more than `5s` to read the request payload (headers, body), drop the connection.  
The implementation part should be filled in the `TODO` blocks.

## Questions
- Can we read from the socket in non blocking way? does it helps us to implement the timeout?
- What happens if the client sends byte by byte in slow periods? can we protect ourselves? (i.e. [Slowloris](https://en.wikipedia.org/wiki/Slowloris_(computer_security)))
- Bonus: How could we also limit server-side processing time (internal timeout)?

## Documentation
- [Python socket module](https://docs.python.org/3.7/library/socket.html)
- [Python time module](https://docs.python.org/3.7/library/time.html)