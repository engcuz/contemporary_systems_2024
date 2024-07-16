# update on July 15, 10:30PM
import threading

import time

# 10 ^ 
LIMIT = 10**6
NUM_THREADS = 4


# global variable to share the result 
results = NUM_THREADS*[0]

# function to calculte the square 
def sum_of_squares(start,end):
    
    total=0
    for i in range(start,end):
        total += i ** 2

    # index is attribute to keep track where thread should write 
    thread_address = threading.current_thread().address #
        # store result of the squre with right address

    results[thread_address] = total

if __name__ == "__main__" :

    #  start time for performace 
    start_time = time.time()
    
    threads = []
    work_size = LIMIT // NUM_THREADS

    #  # splitting the thread for the work 
    for i in range(NUM_THREADS) :
        # start with first index of current thread 
        start = i*work_size
# # find end of range for current thread, to check if  the last thread reaches LIMIT

        end =(i + 1) * work_size if i != NUM_THREADS - 1 else LIMIT

        # Create and start threads
        thread = threading.Thread(target=sum_of_squares, args=(start, end))
        # assign attribute to eacj thread 
        thread.address = i  #
        # append and start the threading 
        threads.append(thread)
        thread.start()

    # dont contiinue unless each threads is finish
    for thread in threads:
        thread.join()
        
    # total sum of squares
    total_sum = sum(results)

    # calcu;ate the  end time after complete 
    end_time = time.time()

    
    print("Sum of squares up to:", LIMIT ,"is : ", total_sum)
    # Calculate execution time
    print("Execution time with threading:", end_time - start_time," seconds")

    # -------------------- Done
