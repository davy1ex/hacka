import socket
import threading

listen_port = 12345
op1_ip = "192.168.0.64"
op3_ip = "192.168.0.25"
received_msg = ""

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
            global received_msg
            received_msg = data.decode()
            print("Received:", received_msg)
        client_socket.close()

def forward_message(target_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((target_ip, listen_port))
    client_socket.send(received_msg.encode())
    client_socket.close()
    print(f"Sent: {received_msg} to {target_ip}")

def user_interface():
    while True:
        user_choice = input("Enter '1' to forward message to op1, '3' to forward message to op3, or 'r' to receive messages: ").lower()
        if user_choice == '1':
            forward_message(op1_ip)
        elif user_choice == '3':
            forward_message(op3_ip)
        elif user_choice == 'r':
            server_thread = threading.Thread(target=server)
            server_thread.start()
            break  # Server will run indefinitely

user_interface()
