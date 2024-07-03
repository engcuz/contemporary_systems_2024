class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.completion_time = None
        self.waiting_time = 0

#SJF
class ProcessByBurstTime(Process):
    def __lt__(self, other):
        return self.burst_time < other.burst_time

#SRTF
class ProcessByRemainingTime(Process):
    def __lt__(self, other):
        return self.remaining_time < other.remaining_time
