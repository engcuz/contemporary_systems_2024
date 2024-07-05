# update July 4th today

# metrics.py
def average_turnaround_time(processes):
    total_turnaround_time = sum(p.completion_time - p.arrival_time for p in processes)
    return total_turnaround_time / len(processes)

def average_waiting_time(processes):
    total_waiting_time = sum(p.waiting_time for p in processes)
    return total_waiting_time / len(processes)

def cpu_utilization(processes):
    total_burst_time = sum(p.burst_time for p in processes)
    total_time = max(p.completion_time for p in processes)
    return (total_burst_time / total_time) * 100
