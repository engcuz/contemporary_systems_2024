# download_files_multiprocessing.py
import multiprocessing
import requests
import time

NUM_PROCESSES = 4

def download_file(url):
    response = requests.get(url)
    return response.text

def process_file(content):
    words = content.split()
    return len(words)

def download_and_process(url, results, index):
    content = download_file(url)
    word_count = process_file(content)
    results[index] = (url, word_count)

if __name__ == "__main__":
    with open("urls.txt") as f:
        urls = [line.strip() for line in f]

    start_time = time.time()
    
    manager = multiprocessing.Manager()
    results = manager.list([None] * len(urls))
    processes = []

    for i, url in enumerate(urls):
        process = multiprocessing.Process(target=download_and_process, args=(url, results, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()
    for url, word_count in results:
        print(f"{url}: {word_count} words")
    print(f"Execution time with multiprocessing: {end_time - start_time} seconds")
