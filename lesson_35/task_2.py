import numpy as np
import threading
import time

def heavy_math_task(size=200, results=None, index=0):
    matrix = np.random.rand(size, size)
    result = np.linalg.det(matrix)
    results[index] = result

def run_threads(n=8):
    start = time.time()
    threads = []
    results = [None] * n
    for i in range(n):
        t = threading.Thread(target=heavy_math_task, args=(200, results, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    end = time.time()
    print("Threads time:", end - start)
    return results

if __name__ == "__main__":
    run_threads()
