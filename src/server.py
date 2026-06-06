import socket
import threading
from .parser import parse_resp
from .commands import handle_command

HOST = "127.0.0.1"
PORT = 6379

def handle_client(conn, addr):
    print(f"Client connected: {addr}")
    with conn:
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                decoded = data.decode("utf-8")
                parts = parse_resp(decoded)
                response = handle_command(parts)
                conn.sendall(response.encode("utf-8"))
            except Exception as e:
                print(f"Error: {e}")
                break
    print(f"Client disconnected: {addr}")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Redis server listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()

if __name__ == "__main__":
    start_server()