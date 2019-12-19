# Level 10: Server Sent Events (SSE streaming)
Implement SSE streaming. An SSE stream has `text/event-stream` content type and is composed of multiple data frames, terminated by newline. The frames have several fields, but it's enough to use only the `data` field.

```
data: some data\n
\n
data: more data\n
\n
```
Every frame needs to be flushed so that the TCP layer will send it immediately to the client.

On the browser side, we have javascript code that connects to the stream and processes it asynchronously.

## Questions
- SSE only streams from the server to the client. How can we send data back to the server?
- How long can we keep the connection open for?
- What are the differences between SSE and websockets?
- What happens if a proxy caches the response? How can we avoid it?

## Documentation
- [SSE on MDN](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)