def parse_resp(data):
    lines = data.split("\r\n")
    result = []
    i = 0

    if not lines or lines[0] == "":
        return result

    if lines[0].startswith("*"):
        num_elements = int(lines[0][1:])
        i = 1
        while i < len(lines) and len(result) < num_elements:
            if lines[i].startswith("$"):
                i += 1
                if i < len(lines):
                    result.append(lines[i])
            i += 1
    else:
        result = lines[0].strip().split()

    return result


def build_resp(value):
    if value is None:
        return "$-1\r\n"
    elif isinstance(value, str):
        return f"+{value}\r\n"
    elif isinstance(value, int):
        return f":{value}\r\n"
    elif isinstance(value, list):
        resp = f"*{len(value)}\r\n"
        for item in value:
            resp += f"${len(item)}\r\n{item}\r\n"
        return resp
    else:
        return "-ERR unknown type\r\n"