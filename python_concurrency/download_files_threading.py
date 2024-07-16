# update on July 15, 10:30PM
import threading
import requests
import time


NUM_THREADS = 4
# download the content of URL
def download_file(url):
    response=requests.get(url)
    return response.text

# process content by counting  number of words
def process_file(content):
    words= content.split()
    return len(words)

# download & process  content of a URL, then store the result 
# index to store  result in  correct place in the shared results list

def download_and_process(url, results, index):
    content= download_file(url)
    word_count= process_file(content)
    results[index ]=(url,word_count)

if __name__ == "__main__":
    with open("urls.txt") as f:
        # strip any whitespces,
        urls = [line.strip() for line in f] 

# start measuring time
    start_time = time.time()
    # list to keep track of the threads
    threads = []

    #create  list with len = to  number of urls
    results = [None] * len(urls)

# ussing enumerate provide both  index i and  url
# to ensure each thread write result to correct position in result 
    for i, url in enumerate(urls):
        thread = threading.Thread(target=download_and_process, args=(url, results, i))
        threads.append(thread)
        thread.start()

    
# # wait for all threads to finish
    for thread in threads:
        thread.join()
# to ,mesuare the end of time after finish the dowlnloading 

    end_time = time.time()

    # print the result 
    for url, word_count in results:
        print(f"{url}: {word_count} words")
    print(f"execution time on threading: {end_time-start_time} seconds")
