import numpy as np
import time

def heavy_math_task(size=200):
    matrix = np.random.rand(size, size)
    return np.linalg.det(matrix)

def run_sequential(n=8):
    start = time.time()
    results = []
    for _ in range(n):
        result = heavy_math_task()
        results.append(result)
    end = time.time()
    print("Время потраченной на выполнение:", end - start)
    return results

if __name__ == "__main__":
    run_sequential()
