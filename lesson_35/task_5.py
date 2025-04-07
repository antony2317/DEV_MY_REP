import requests
import threading
import time

URLS = [f"https://httpbin.org/get?query={i}" for i in range(5)]
results = [None] * len(URLS)

def fetch(index, url):
    response = requests.get(url)
    results[index] = response.status_code

def run_threads(urls):
    start = time.time()
    threads = []
    for i, url in enumerate(urls):
        thread = threading.Thread(target=fetch, args=(i, url))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()
    print("Threads time:", end - start)
    return results

if __name__ == "__main__":
    run_threads(URLS)
