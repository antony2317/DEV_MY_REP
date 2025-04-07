import requests
import multiprocessing
import time

URLS = [f"https://httpbin.org/get?query={i}" for i in range(5)]

def fetch(url, queue):
    response = requests.get(url)
    queue.put(response.status_code)

def run_processes(urls):
    start = time.time()
    processes = []
    queue = multiprocessing.Queue()
    for url in urls:
        p = multiprocessing.Process(target=fetch, args=(url, queue))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    results = [queue.get() for _ in urls]
    end = time.time()
    print("Processes time:", end - start)
    return results

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    run_processes(URLS)
