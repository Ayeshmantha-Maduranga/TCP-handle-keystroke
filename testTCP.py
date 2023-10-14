import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 65432))
sock.listen()

conn, addr = sock.accept()
with conn:
    while True:
        data = conn.recv(1024)
        print(data)
        if not data:
            break

sock.close()