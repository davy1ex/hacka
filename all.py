import socket
import threading

# Параметры сети
listen_port = 12345
forward_port = 12345

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
            print("Received:", data.decode())
        client_socket.close()

def send_message_to_server(ip_server):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip_server, listen_port))
    message = input("Enter your message: ")
    client_socket.send(message.encode())
    client_socket.close()

def user_interface():
    while True:
        user_choice = input("Enter 's' to send a message or 'r' to receive messages: ").lower()
        if user_choice == 's':
            ip_server = input("Enter the IP address of the server: ")
            send_message_to_server(ip_server)
        elif user_choice == 'r':
            server_thread = threading.Thread(target=server)
            server_thread.start()
            break  # Exit the user interface loop as the server will run indefinitely
        else:
            print("Invalid choice. Please try again.")

# Start the user interface
user_interface()
