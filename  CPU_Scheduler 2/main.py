# update July 5th today 11:50PM

#1 0 4 2 
#2 2 6 1
#3 4 4 3
#4 6 5 2
#5 10 2 1




# main.py
import metrics

from process import Process
from scheduler import Scheduler
 
 # read input from  text file
def read_input(file_path='input.txt'):
    # define empty list 
    processes = [] 

    with  open(file_path, 'r') as file:
        for line in file :
            # use to read file with spaces , then conver to int
            pid, arrival_time,burst_time,priority=  map(int, line.split())
            processes.append(Process(pid, arrival_time, burst_time, priority))
    return  processes

# func to print all the result for all methods 
def print_results(algorithm_name, scheduled_processes):
    print(" Algorithm",algorithm_name)
    print(f"A verage Turnaround Time: {metrics.average_turnaround_time(scheduled_processes):.2f}")
    print(f" Average Waiting Time : {metrics.average_waiting_time(scheduled_processes):.2f}")
    print(f"CPU Utilization : {metrics.cpu_utilization(scheduled_processes):.2f}%")
    for process in scheduled_processes:
        print(f"Process {process.pid} - Completion Time: {process.completion_time}, Waiting Time: {process.waiting_time}")
    print()

def main():
    # read from the input
    processes = read_input()
    scheduler = Scheduler(processes)

    # call FCFS
    scheduled_processes_fcfs = scheduler.fcfs()
    print_results("first-Come, first-Served", scheduled_processes_fcfs)

    # call SJF
    processes = read_input()
    scheduler = Scheduler(processes)
    scheduled_processes_sjf = scheduler.sjf()
    print_results("shortest jhob first", scheduled_processes_sjf)

    # call SRTF
    processes = read_input()
    scheduler = Scheduler(processes)
    scheduled_processes_srtf = scheduler.srtf()
    print_results("Shortest Remaining Time First", scheduled_processes_srtf)

    # Run and print results for Round Robin with quantum 2
    processes = read_input()  # Reset processes for RR
    scheduler = Scheduler(processes)
    scheduled_processes_rr = scheduler.rr(quantum=2)
    print_results("Round Robin (Quantum = 2)", scheduled_processes_rr)

    # call Priority (Preemptive)
    processes = read_input()  # Reset processes for Priority
    scheduler = Scheduler(processes)
    scheduled_processes_priority_preemptive = scheduler.priority(preemptive=True)
    print_results("Priority Scheduling (Preemptive)", scheduled_processes_priority_preemptive)

    # call Priority (Non-Preemptive)
    processes = read_input()  # Reset processes for Priority
    scheduler = Scheduler(processes)
    scheduled_processes_priority_non_preemptive = scheduler.priority(preemptive=False)
    print_results("Priority Scheduling (Non-Preemptive)", scheduled_processes_priority_non_preemptive)

if __name__ == '__main__':
    main() # call/ excute tge main function
