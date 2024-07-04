# main.py
from process import Process
from scheduler import Scheduler
import metrics

def read_input(file_path='input.txt'):
    processes = []
    with open(file_path, 'r') as file:
        for line in file:
            pid, arrival_time, burst_time, priority = map(int, line.split())
            processes.append(Process(pid, arrival_time, burst_time, priority))
    return processes

def print_results(algorithm_name, scheduled_processes):
    print(f"Algorithm: {algorithm_name}")
    print(f"Average Turnaround Time: {metrics.average_turnaround_time(scheduled_processes):.2f}")
    print(f"Average Waiting Time: {metrics.average_waiting_time(scheduled_processes):.2f}")
    print(f"CPU Utilization: {metrics.cpu_utilization(scheduled_processes):.2f}%")
    for process in scheduled_processes:
        print(f"Process {process.pid} - Completion Time: {process.completion_time}, Waiting Time: {process.waiting_time}")
    print()

def main():
    processes = read_input()
    scheduler = Scheduler(processes)

    # Run and print results for FCFS
    scheduled_processes_fcfs = scheduler.fcfs()
    print_results("First-Come, First-Served", scheduled_processes_fcfs)

    # Run and print results for SJF
    processes = read_input()
    scheduler = Scheduler(processes)
    scheduled_processes_sjf = scheduler.sjf()
    print_results("Shortest Job First", scheduled_processes_sjf)

    # Run and print results for SRTF
    processes = read_input()
    scheduler = Scheduler(processes)
    scheduled_processes_srtf = scheduler.srtf()
    print_results("Shortest Remaining Time First", scheduled_processes_srtf)

    # Run and print results for Round Robin with quantum 2
    processes = read_input()  # Reset processes for RR
    scheduler = Scheduler(processes)
    scheduled_processes_rr = scheduler.rr(quantum=2)
    print_results("Round Robin (Quantum = 2)", scheduled_processes_rr)

    # Run and print results for Priority (Preemptive)
    processes = read_input()  # Reset processes for Priority
    scheduler = Scheduler(processes)
    scheduled_processes_priority_preemptive = scheduler.priority(preemptive=True)
    print_results("Priority Scheduling (Preemptive)", scheduled_processes_priority_preemptive)

    # Run and print results for Priority (Non-Preemptive)
    processes = read_input()  # Reset processes for Priority
    scheduler = Scheduler(processes)
    scheduled_processes_priority_non_preemptive = scheduler.priority(preemptive=False)
    print_results("Priority Scheduling (Non-Preemptive)", scheduled_processes_priority_non_preemptive)

if __name__ == '__main__':
    main()
