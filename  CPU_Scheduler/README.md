# Contemporary_Systems_2024
## Getting started


### Files and Their Purpose

1. **process.py**:
   - Contains the `Process` class that defines the attributes of a process, including `pid`, `arrival_time`, `burst_time`, `priority`, `remaining_time`, `completion_time`, and `waiting_time`.

2. **scheduler.py**:
   - Contains the `Scheduler` class with methods for different scheduling algorithms:
     - `fcfs(self)`: First-Come, First-Served
     - `sjf(self)`: Shortest Job First (non-preemptive)
     - `srtf(self)`: Shortest Remaining Time First (preemptive)
     - `rr(self, quantum)`: Round Robin with a given quantum
     - `priority(self, preemptive=False)`: Priority Scheduling (both preemptive and non-preemptive versions)

3. **metrics.py**:
   - Contains functions to calculate performance metrics:
     - `average_turnaround_time(processes)`: Calculates the average turnaround time
     - `average_waiting_time(processes)`: Calculates the average waiting time
     - `cpu_utilization(processes)`: Calculates CPU utilization

4. **main.py**:
   - The main program that reads process data from an input file, creates `Process` objects, initializes a `Scheduler`, runs each scheduling algorithm, and calculates and displays performance metrics for each algorithm.

## How to Run

1. Ensure you have Python installed on your system.
2. Place your input data in a file named `input.txt` in the following format:
    ```
    1 0 10 3
    2 1 5 1
    3 3 8 2
    ...
    ```
    Each line represents a process with the following fields:
    - Process ID
    - Arrival Time
    - Burst Time
    - Priority
3. Navigate to the `cpu_scheduler` directory and run the `main.py` script:
    
    python main.py
    

## Example Output

The program will output results in the following format:



Algorithm Shortest Remaining Time First
A verage Turnaround Time: 7.60
Average Waiting Time : 3.40
CPU Utilization : 100.00%
Process 1 - Completion Time: 4, Waiting Time: 0
Process 3 - Completion Time: 8, Waiting Time: 0
Process 5 - Completion Time: 12, Waiting Time: 0
Process 4 - Completion Time: 15, Waiting Time: 4
Process 2 - Completion Time: 21, Waiting Time: 13