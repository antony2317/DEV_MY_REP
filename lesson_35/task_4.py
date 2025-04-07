import requests
import time

URLS = [f"https://httpbin.org/get?query={i}" for i in range(5)]

def fetch(url):
    response = requests.get(url)
    return response.status_code

def run_sequential(urls):
    start = time.time()
    results = []
    for url in urls:
        results.append(fetch(url))
    end = time.time()
    print("Sequential time:", end - start)
    return results

if __name__ == "__main__":
    run_sequential(URLS)
