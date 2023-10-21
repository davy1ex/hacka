import socket

def main():
    op2_ip = '192.168.100.72'  # Замените на реальный IP-адрес op2
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((op2_ip, 12345))

    message = "жопа жопы"
    client_socket.send(message.encode())

    client_socket.close()

if __name__ == "__main__":
    main()