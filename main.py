import socket


def get_own_ip():
    # Получение своего IP-адреса
    hostname = socket.gethostname()
    own_ip = socket.gethostbyname(hostname)
    return own_ip


def get_ip_of_host(host_name):
    # Получение IP-адреса другого устройства по его имени хоста
    try:
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except socket.gaierror:
        print(f"Unable to resolve host: {host_name}")
        return None


def main():
    own_ip = get_own_ip()
    print(f"My IP Address: {own_ip}")

    # Предполагая, что имена хостов известны и разрешаемы
    op2_host_name = 'op2.local'
    op2_ip = '192.168.100.72'  # Замените на реальный IP-адрес op2

    op3_host_name = 'op3.local'

    # op2_ip = get_ip_of_host(op2_host_name)
    op3_ip = get_ip_of_host(op3_host_name)

    if op2_ip:
        print(f"IP Address of op2: {op2_ip}")
    if op3_ip:
        print(f"IP Address of op3: {op3_ip}")


if __name__ == "__main__":
    main()
