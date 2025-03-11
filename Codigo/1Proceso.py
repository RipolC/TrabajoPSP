import time

def compute_pi(N):
    """Calcula la aproximación de Pi usando integración numérica."""
    step = 1.0 / N
    sum_ = 0.0
    for i in range(N):
        x = (i + 0.5) * step
        sum_ += 4.0 / (1.0 + x * x)
    return sum_ * step

if _name_ == "_main_":
    # Paso 1: Ejecutar una prueba con un pequeño N
    test_N = 1000000  # 1 millón de intervalos para medir el tiempo
    start_time = time.time()
    compute_pi(test_N)
    test_time = time.time() - start_time

    # Paso 2: Estimar el valor inicial de N para durar entre 59.8 y 60.2 segundos
    estimated_N = int((60 / test_time) * test_N)
    print(f"Estimando N ≈ {estimated_N} para durar 60 segundos...\n")

    # Paso 3: Ejecutar el cálculo y ajustar el N para que dure entre 59.8 y 60.2 segundos
    elapsed_time = 0
    while elapsed_time < 59.8 or elapsed_time > 60.2:
        start_time = time.time()
        pi_total = compute_pi(estimated_N)
        elapsed_time = time.time() - start_time
        
        # Ajustar el número de intervalos si el tiempo es muy bajo o muy alto
        if elapsed_time < 59.8:
            estimated_N = int(estimated_N * (60 / elapsed_time))  # Incrementar N
        elif elapsed_time > 60.2:
            estimated_N = int(estimated_N * (60 / elapsed_time))  # Reducir N

    # Mostrar resultado final
    print(f"Aproximación de Pi después de 60 segundos: {pi_total:.15f}")
    print(f"Tiempo total de ejecución: {elapsed_time:.4f} segundos")
