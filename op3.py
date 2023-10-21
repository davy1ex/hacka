import socket

listen_port = 12345
op2_ip = "192.168.0.12"

def send_message_to_op2(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((op2_ip, listen_port))
    client_socket.send(message.encode())
    client_socket.close()
    print(f"Sent: {message} to op2")

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
            if client_address[0] == op2_ip:
                send_message_to_op2(received_msg)  # Automatically send the message back to op2
        client_socket.close()

server()  # Automatically start in receive mode
