# sum_of_squares_threading.py
import threading
import time

NUM_THREADS = 4
LIMIT = 10**6

def sum_of_squares(start, end, result, index):
    total = 0
    for num in range(start, end):
        total += num ** 2
    result[index] = total

if __name__ == "__main__":
    start_time = time.time()
    
    threads = []
    results = [0] * NUM_THREADS
    chunk_size = LIMIT // NUM_THREADS

    for i in range(NUM_THREADS):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != NUM_THREADS - 1 else LIMIT
        thread = threading.Thread(target=sum_of_squares, args=(start, end, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_sum = sum(results)
    end_time = time.time()
    print(f"Sum of squares up to {LIMIT}: {total_sum}")
    print(f"Execution time with threading: {end_time - start_time} seconds")
