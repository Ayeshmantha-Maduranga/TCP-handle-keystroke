import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 65432))
server_socket.listen()

conn, addr = server_socket.accept()
with conn:
    while True:
        data = conn.recv(1024)
        print(data)
        if not data:
            break

server_socket.close()
