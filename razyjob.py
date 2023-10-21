import socket
import threading
import time

# Переменные для настройки
ip_server = "192.168.100.93"
next_ip = "192.168.100.97"
listen_port = 12345
forward_port = 12345


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', listen_port))
    server_socket.listen(1)

    while True:
        print("Waiting for connection on port")
        
        client_socket, client_address = server_socket.accept()
        print("Accepted connection")

        data = client_socket.recv(1024)
        if data:
            print("Received", data.decode())
            forward(data)

        client_socket.close()  
	

def forward(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((next_ip, forward_port))
    client_socket.send(data)
    client_socket.close()
    print("Data forwarded to", next_ip)


def send_message_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip_server, listen_port))
    message = input("Enter your message: ")
    client_socket.send(message.encode())
    client_socket.close()


server_thread = threading.Thread(target=server)
server_thread.start()


time.sleep(2)


while True:
    send_message_to_server()
