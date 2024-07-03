from scheduler import Scheduler


def average_turnaround_time(processes):
    sum_turned_time = 0
    for i in range(len(processes)):
        sum_turned_time = sum_turned_time + (processes[i].completion_time - processes[i].arrival_time)
    avg_turned_time = sum_turned_time / len(processes)
    return avg_turned_time


def average_waiting_time(processes):
    sum_waiting_times = 0
    for i in range(len(processes)):
        sum_waiting_times = sum_waiting_times + processes[i].waiting_time
    avg_waiting_time = sum_waiting_times / len(processes)
    return avg_waiting_time


def cpu_utilization(processes):
    total_burst_time = 0
    for i in range(len(processes)):
        total_burst_time = total_burst_time + processes[i].burst_time
    CPU = (total_burst_time / (processes[len(processes) - 1].completion_time - processes[0].arrival_time)) * 100
    return CPU
