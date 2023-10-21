import socket

listen_port = 12345
op1_ip = "192.168.0.64"
op3_ip = "192.168.0.25"

def forward_message(target_ip, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target_ip, listen_port))
    client_socket.send(message.encode())
    client_socket.close()
    print(f"Sent: {message} to {target_ip}")

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', listen_port))
    server_socket.listen(1)
    print("Waiting for connection on port", listen_port)

    while True:
        client_socket, client_address = server_socket.accept()
        print("Accepted connection from", client_address)
        data = client_socket.recv(1024)
        if data:
            received_msg = data.decode()
            print("Received:", received_msg)
            target_ip = op3_ip if client_address[0] == op1_ip else op1_ip
            forward_message(target_ip, received_msg)  # Automatically forward the message
        client_socket.close()

server()  # Automatically start in receive mode
