# update on July 15, 10:50PM


import multiprocessing
import time

NUM_PROCESSES = 4
LIMIT = 10**6

# function to calculte the square 

def sum_of_squares(start,end):
    return sum(num ** 2 for num in range(start, end))

if __name__ == "__main__":

    # start time for performace measure 

    start_time= time.time()
    
    # create pool space for processes / Pool : to parallelize  execution of the function 
    worker_pool = multiprocessing.Pool(processes=NUM_PROCESSES)
    
    # calculate  work size load for each process
    work_size = LIMIT//NUM_PROCESSES

#create list of (start,end) tupls for each process
    work_ranges =[(i *work_size,(i+1)*work_size) for i in range(NUM_PROCESSES ) ]
    # to make sure it reach the limit 
    work_ranges[-1] = (work_ranges[-1][0], LIMIT)  
    
    # starmap to allow parallel execution of the function  sum_of_squares
    results=worker_pool.starmap(sum_of_squares, work_ranges)
    
    #      # total sum of squares

    total_sum = sum(results)
    
    # calcu;ate the  end time after complete 

    end_time = time.time()
   
    print("Sum of squares up to:", LIMIT ,"is : ", total_sum)
    # Calculate execution time
    print("Execution time with multiprocessing:", end_time - start_time," seconds")

    # Done 
