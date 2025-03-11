import socket
import struct
import time

SERVER_IP = "10.20.20.100"  # Reemplaza con la IP del servidor
PORT = 65432

def compute_pi(client_id, num_clients):
    """Cada cliente calcula una parte de la serie de Leibniz."""
    local_sum = 0.0
    i = client_id  # Cada cliente empieza en su índice correspondiente
    sign = 1 if i % 2 == 0 else -1  # Alternancia de signos

    start_time = time.time()
    end_time = start_time + 60  # Ejecutar por 1 minuto

    while time.time() < end_time:
        term = sign * (1 / (2 * i + 1))
        local_sum += term
        i += num_clients  # Saltar términos ya asignados a otros clientes
        sign *= -1  # Alternar signo

    return local_sum

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

# Recibir el índice del cliente y la cantidad total de clientes
data = client.recv(8)  # 4 bytes para client_id + 4 bytes para num_clients
if data:
    client_id, num_clients = struct.unpack("ii", data)

    # Calcular Pi parcial
    result = compute_pi(client_id, num_clients)

    # Enviar resultado al servidor
    client.sendall(struct.pack("d", result))

client.close()
