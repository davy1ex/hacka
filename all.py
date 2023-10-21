import socket
import threading

# Параметры сети
listen_port = 12345

# Объявление объекта события для контроля над серверным потоком
stop_server_event = threading.Event()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', listen_port))
    server_socket.listen(1)
    print("Waiting for connection on port", listen_port)

    while not stop_server_event.is_set():
        # Установка таймаута для accept, чтобы проверить stop_server_event
        server_socket.settimeout(1)
        try:
            client_socket, client_address = server_socket.accept()
        except socket.timeout:
            continue  # Проверить stop_server_event снова

        print("Accepted connection from", client_address)
        data = client_socket.recv(1024)
        if data:
            print("Received:", data.decode())
        client_socket.close()

    server_socket.close()  # Закрываем сокет при выходе

def send_message_to_server(ip_server):
    while True:
        message = input("Enter your message (or type 'exit' to go back): ")
        if message.lower() == 'exit':
            break  # Выход из режима отправки сообщений
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip_server, listen_port))
        client_socket.send(message.encode())
        client_socket.close()

def user_interface():
    while True:
        user_choice = input("Enter 's' to send a message, 'r' to receive messages, or 'q' to quit: ").lower()
        if user_choice == 's':
            ip_server = input("Enter the IP address of the server: ")
            send_message_to_server(ip_server)
        elif user_choice == 'r':
            stop_server_event.clear()  # Сбросить событие перед запуском сервера
            server_thread = threading.Thread(target=server)
            server_thread.start()
            input("Press Enter to go back...")
            stop_server_event.set()  # Установить событие для остановки сервера
            server_thread.join()  # Дождаться завершения серверного потока
        elif user_choice == 'q':
            if server_thread.is_alive():
                stop_server_event.set()  # Установить событие для остановки сервера, если он запущен
                server_thread.join()  # Дождаться завершения серверного потока
            break  # Выход из интерфейса пользователя
        else:
            print("Invalid choice. Please try again.")

# Запуск пользовательского интерфейса
user_interface()
