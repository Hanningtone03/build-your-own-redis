# Build Your Own Redis

A Redis clone built from scratch in Python using raw TCP sockets and the RESP protocol — no Redis libraries used.

## How it works

Redis is an in-memory key-value store that communicates over TCP using a protocol called RESP. This project implements that from scratch:

- Opens a raw TCP socket on port 6379 (same port as real Redis)
- Parses incoming RESP protocol messages manually
- Stores key-value pairs in memory with optional TTL expiry
- Handles multiple clients simultaneously using threads

## Project structure
## Running locally

```bash
python -m src.server
```

## Supported commands

| Command | Example | Description |
|---------|---------|-------------|
| PING | `PING` | Check if server is alive |
| SET | `SET name John` | Store a value |
| SET with TTL | `SET name John EX 10` | Store a value that expires in 10 seconds |
| GET | `GET name` | Retrieve a value |
| DEL | `DEL name` | Delete a key |
| EXISTS | `EXISTS name` | Check if a key exists |

## Tech

- Python 3
- `socket` module (raw TCP)
- `threading` module (concurrent clients)
- No external dependencies