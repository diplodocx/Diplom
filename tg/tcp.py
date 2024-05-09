import socket

HOST = "127.0.0.1"
PORT = 65432


def send_tcp_request(text: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(bytes(text, 'utf-8'))
        data = s.recv(1024)
        return str(data, 'utf-8')
