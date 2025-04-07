import numpy as np
import multiprocessing
import time

def heavy_math_task(queue, size=200):
    matrix = np.random.rand(size, size)
    result = np.linalg.det(matrix)
    queue.put(result)

def run_processes(n=8):
    start = time.time()
    processes = []
    queue = multiprocessing.Queue()
    for _ in range(n):
        p = multiprocessing.Process(target=heavy_math_task, args=(queue,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    results = [queue.get() for _ in range(n)]
    end = time.time()
    print("Processes time:", end - start)
    return results

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_processes()
