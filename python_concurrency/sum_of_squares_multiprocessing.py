# sum_of_squares_multiprocessing.py
import multiprocessing
import time

NUM_PROCESSES = 4
LIMIT = 10**6

def sum_of_squares(start, end, result, index):
    total = 0
    for num in range(start, end):
        total += num ** 2
    result[index] = total

if __name__ == "__main__":
    start_time = time.time()
    
    processes = []
    manager = multiprocessing.Manager()
    results = manager.list([0] * NUM_PROCESSES)
    chunk_size = LIMIT // NUM_PROCESSES

    for i in range(NUM_PROCESSES):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != NUM_PROCESSES - 1 else LIMIT
        process = multiprocessing.Process(target=sum_of_squares, args=(start, end, results, i))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_sum = sum(results)
    end_time = time.time()
    print(f"Sum of squares up to {LIMIT}: {total_sum}")
    print(f"Execution time with multiprocessing: {end_time - start_time} seconds")
