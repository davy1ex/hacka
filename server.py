import socket

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Слушаем на всех доступных интерфейсах
    server_socket.listen()

    print("Ожидание подключения...")
    client_socket, client_address = server_socket.accept()
    print(f"Подключение от {client_address}")

    data = client_socket.recv(1024)
    print(f"Получено: {data.decode()}")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()