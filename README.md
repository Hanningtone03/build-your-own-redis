# Build Your Own Redis

A Redis clone built from scratch in Python using raw TCP sockets and the RESP protocol — no Redis libraries used.

## How it works

Redis is an in-memory key-value store that communicates over TCP using a protocol called RESP. This project implements that from scratch:

- Opens a raw TCP socket on port 6379 (same port as real Redis)
- Parses incoming RESP protocol messages manually
- Stores key-value pairs in memory with optional TTL expiry
- Handles multiple clients simultaneously using threads

## Project structure
