![CI](https://github.com/Hanningtone03/build-your-own-redis/actions/workflows/ci.yml/badge.svg)

# Build Your Own Redis

A Redis clone in Python using raw TCP sockets and the RESP protocol; no Redis libraries.

## How it works

A TCP server on port 6379 that reads RESP-encoded commands, executes them against an in-memory dictionary, and writes RESP responses back. Keys can expire via TTL. Multiple clients handled via threads.

## Project structure

```
src/
├── server.py
├── parser.py
├── commands.py
└── store.py
```

## Running locally

```bash
python -m src.server
```

## Supported commands

| Command | Example |
|---------|---------|
| PING | `PING` |
| SET | `SET name John` |
| SET with TTL | `SET name John EX 10` |
| GET | `GET name` |
| DEL | `DEL name` |
| EXISTS | `EXISTS name` |

## Tech

- Python 3
- `socket`, `threading` modules
- No external dependencies
