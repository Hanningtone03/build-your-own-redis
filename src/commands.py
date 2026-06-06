from .store import Store

store = Store()

def handle_command(parts):
    if not parts:
        return "-ERR empty command\r\n"

    command = parts[0].upper()

    if command == "PING":
        return "+PONG\r\n"

    elif command == "SET":
        if len(parts) < 3:
            return "-ERR wrong number of arguments for SET\r\n"
        key, value = parts[1], parts[2]
        ttl = None
        if len(parts) == 5 and parts[3].upper() == "EX":
            ttl = int(parts[4])
        store.set(key, value, ttl)
        return "+OK\r\n"

    elif command == "GET":
        if len(parts) < 2:
            return "-ERR wrong number of arguments for GET\r\n"
        value = store.get(parts[1])
        if value is None:
            return "$-1\r\n"
        return f"${len(value)}\r\n{value}\r\n"

    elif command == "DEL":
        if len(parts) < 2:
            return "-ERR wrong number of arguments for DEL\r\n"
        result = store.delete(parts[1])
        return f":{result}\r\n"

    elif command == "EXISTS":
        if len(parts) < 2:
            return "-ERR wrong number of arguments for EXISTS\r\n"
        result = 1 if store.exists(parts[1]) else 0
        return f":{result}\r\n"

    else:
        return f"-ERR unknown command '{command}'\r\n"