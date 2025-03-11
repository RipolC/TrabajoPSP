import socket
import struct
import time

HOST = "0.0.0.0"  # Acepta conexiones desde cualquier IP
PORT = 65432
NUM_CLIENTES = 3  # Número de clientes esperados

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(NUM_CLIENTES)

print(f"Servidor esperando {NUM_CLIENTES} clientes en {HOST}:{PORT}...")

clientes = []
for i in range(NUM_CLIENTES):
    conn, addr = server.accept()
    print(f"Cliente conectado desde {addr}")
    clientes.append((conn, i))  # Guardar conexión y su índice

# Enviar a cada cliente su ID y el número total de clientes
for conn, client_id in clientes:
    conn.sendall(struct.pack("ii", client_id, NUM_CLIENTES))

# Iniciar medición de tiempo
start_time = time.time()
end_time = start_time + 60  # Ejecutar por 1 minuto
total_pi = 0.0

while time.time() < end_time:
    for conn, _ in clientes:
        # Recibir resultado parcial del cliente
        data = conn.recv(8)
        if data:
            total_pi += struct.unpack("d", data)[0]

# Calcular Pi final
pi_total = 4 * total_pi
elapsed_time = time.time() - start_time

print(f"Aproximación de Pi después de 1 minuto: {pi_total:.15f}")
print(f"Tiempo total de ejecución: {elapsed_time:.4f} segundos")

# Cerrar conexiones
for conn, _ in clientes:
    conn.close()

server.close()
