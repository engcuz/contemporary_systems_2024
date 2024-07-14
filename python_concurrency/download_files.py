# download_files.py
import requests
import time

def download_file(url):
    response = requests.get(url)
    return response.text

def process_file(content):
    words = content.split()
    return len(words)

def download_and_process_files(urls):
    results = []
    for url in urls:
        content = download_file(url)
        word_count = process_file(content)
        results.append((url, word_count))
    return results

if __name__ == "__main__":
    with open("urls.txt") as f:
        urls = [line.strip() for line in f]

    start_time = time.time()
    results = download_and_process_files(urls)
    end_time = time.time()
    
    for url, word_count in results:
        print(f"{url}: {word_count} words")
    
    print(f"Execution time (non-concurrent): {end_time - start_time} seconds")
