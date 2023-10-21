import socket
import threading

listen_port = 12345
op2_ip = "192.168.0.12"
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

def send_message_to_op2():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((op2_ip, listen_port))
    client_socket.send(received_msg.encode())
    client_socket.close()
    print(f"Sent: {received_msg} to op2")

def user_interface():
    while True:
        user_choice = input("Enter 's' to send a message to op2 or 'r' to receive messages: ").lower()
        if user_choice == 's':
            send_message_to_op2()
        elif user_choice == 'r':
            server_thread = threading.Thread(target=server)
            server_thread.start()
            break  # Server will run indefinitely

user_interface()
