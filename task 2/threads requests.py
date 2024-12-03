import requests
import multiprocessing
import time

def fetch_url(url):
    response = requests.get(url)
    return response.text

def fetch_all(urls):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(fetch_url, urls)
    return results

def main():
    urls = ["https://jsonplaceholder.typicode.com/posts/1"] * 150
    start_time = time.time()
    results = fetch_all(urls)
    print(f"Fetched {len(results)} pages.")
    print("Time taken (multiprocessing):", time.time() - start_time)

if __name__ == "__main__":
    main()
