import socket
import matplotlib.pyplot as plt
import numpy as np

# Создание сокета
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 65432))
server_socket.listen()

print('Ожидание соединения...')
conn, addr = server_socket.accept()
print(f'Соединение с {addr}')

values = []  # Список для хранения полученных значений

with conn:
    while True:
        data = conn.recv(1024)
        if not data:
            break  # Выход из цикла, если данные не поступают
        value = float(data.decode().strip())
        print('getted', value)
        values.append(value)

# Построение графика
if values:
    x = np.arange(len(values))
    plt.plot(x, values)
    plt.show()

server_socket.close()
