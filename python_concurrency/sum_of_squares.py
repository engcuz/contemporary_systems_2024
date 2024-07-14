# sum_of_squares.py
import time

def sum_of_squares(limit):
    total = 0
    for num in range(limit):
        total += num ** 2
    return total

if __name__ == "__main__":
    limit = 1000000
    
    start_time = time.time()
    result = sum_of_squares(limit)
    end_time = time.time()
    
    print(f"Sum of squares up to {limit}: {result}")
    print(f"Execution time (non-concurrent): {end_time - start_time} seconds")




