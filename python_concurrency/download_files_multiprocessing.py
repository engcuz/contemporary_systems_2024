# update on July 15, 10:50PM
#Albernawi
#COMP 4704
import multiprocessing
import requests
import time

NUM_PROCESSES = 6

# download  content of a url.
def download_file(url):
    response = requests.get(url)
    return response.text

# Process  content by counting  number of words
def process_file(content):
    words =content.split()
    return len(words)


 # download & process content of urls & store the result
def download_and_process(url, results, index):
    content = download_file(url)
    word_count = process_file(content)

    #index to store  result in correct place in the shared results list

    results[index]=(url, word_count)

if __name__ == "__main__":
    with open("urls.txt") as f:
        # strip any whitespces,

        urls=[line.strip() for line in f ]


# start measuring time

    start_time = time.time()
    
    #using Manager method allows different processes to share data 
    # such as like lists, dictionaries
    manager = multiprocessing.Manager()
    # shared result list , length == to the number of urls
    results=manager.list([None]*len(urls))

    # list is used  to keep track of all  process objects 
    processes=[]

    for i,url in enumerate(urls):
        # create & start new process for each url
        process =multiprocessing.Process(target=download_and_process,args=(url, results, i))

# created process is appended to other processes
        processes.append(process )

        #begins executing  download_and_process
        process.start()
## # wait for all threads to finish

    for process in processes:
        process.join()


# to ,mesuare the end of time after finish the dowlnloading 

    end_time = time.time()

        # print the result 

    for url, word_count in results:
        print(f"{url}: {word_count} words")

    print("Execution time on multiprocessing: ",end_time-start_time," seconds")
