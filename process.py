# process.py
class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0, completion_time=None, waiting_time=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.completion_time = completion_time
        self.waiting_time = waiting_time

    def __lt__(self, other):
        return self.burst_time < other.burst_time

    def __eq__(self, other):
        return (self.pid == other.pid and self.arrival_time == other.arrival_time and
                self.burst_time == other.burst_time and self.priority == other.priority and
                self.remaining_time == other.remaining_time and self.completion_time == other.completion_time and
                self.waiting_time == other.waiting_time)

    def __repr__(self):
        return (f"Process({self.pid}, {self.arrival_time}, {self.burst_time}, {self.priority}, "
                f"completion_time={self.completion_time}, waiting_time={self.waiting_time})")
