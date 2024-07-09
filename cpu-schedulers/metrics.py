# update July 5th today 11:40PM
# update July 9th today 1:40 PM
#moved 
# metrics.py
# 
# calculate different between  completion time and arrival time of each process.
def average_turnaround_time(processes):
    total_turnaround_time = sum(p.completion_time - p.arrival_time for p in processes)
    return total_turnaround_time / len(processes)
# calculate total time when process  in system waiting to be execute
def average_waiting_time(processes):
    total_waiting_time = sum(p.waiting_time for p in processes)
    return total_waiting_time / len(processes)

 # calculate  CPU utilization percentage, which when cpu being used oposit to not or wait 
def cpu_utilization(processes):
    total_burst_time = sum(p.burst_time for p in processes)
    total_time = max(p.completion_time for p in processes) - min(p.arrival_time for p in processes)
    return (total_burst_time / total_time) * 100

