import socket
import time
import numpy as np


mu, sigma, num_samples = 0, 0.1, 100  # среднее значение, стандартное отклонение, количество выборок
data = np.random.normal(mu, sigma, num_samples)
# Создание сокета
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 65432))

# Отправка данных
# data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
for value in data:
    client_socket.sendall(f"{value}".encode())
    time.sleep(0.5)  # Задержка между отправкой данных (опционально)

client_socket.close()
