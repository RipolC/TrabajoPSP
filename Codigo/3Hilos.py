import threading
import time

N = 100000000  # Número total de intervalos
num_threads = 3  # Número de hilos
results = [0.0] * num_threads  # Para almacenar resultados parciales
threads = []  # Lista de hilos

def compute_pi(start, end, index):
    """Calcula una parte del valor de Pi."""
    step = 1.0 / N
    sum_ = 0.0
    for i in range(start, end):
        x = (i + 0.5) * step
        sum_ += 4.0 / (1.0 + x * x)
    results[index] = sum_ * step

if _name_ == "_main_":
    start_time = time.time()  # ⏱ Iniciar medición

    chunk = N // num_threads  # Dividir el trabajo entre los hilos
    for i in range(num_threads):
        start = i * chunk
        end = (i + 1) * chunk if i != num_threads - 1 else N
        thread = threading.Thread(target=compute_pi, args=(start, end, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Esperar a que todos los hilos terminen

    pi_total = sum(results)  # Sumar resultados de los hilos

    end_time = time.time()  # ⏱ Finalizar medición
    elapsed_time = end_time - start_time

    print(f"Aproximación de Pi: {pi_total:.15f}")
    print(f"Tiempo total de ejecución: {elapsed_time:.4f} segundos")
