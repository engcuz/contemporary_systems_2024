# Start 2024

from process import Process, ProcessByBurstTime, ProcessByRemainingTime
from scheduler import Scheduler
from metrics import average_waiting_time, average_waiting_time, cpu_utilization



#read from file read function
#Use split pid, atime, btime, priority
with open(filename, 'r'):




p1 = Process(1, 0, 4, 2)
p2 = Process(2, 2, 6, 1)
p3 = Process(3, 4, 4, 3)
p4 = Process(4, 6, 5, 2)
p5 = Process(5, 10, 2, 1)

proc = [p1, p2, p3, p4, p5]

s = Scheduler(proc)


updated = s.priority(True)

for i in range(len(updated)):
    print(f" The completion time for Process {i} is : {updated[i].completion_time}")
    print(f" The waiting time for Process {i} is : {updated[i].waiting_time}")