# # update July 5th today 11:40PM


class Process:
    #define the methods and the objects/ attributs 
    def __init__(self, pid, arrival_time, burst_time, priority=0, completion_time=None, waiting_time=0):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.completion_time = completion_time
        self.waiting_time = waiting_time

# to compare processe based on burst time
    def __lt__(self, other):
        return self.burst_time < other.burst_time
# to compare process with other based on multiple attributes
    def __eq__(self, other):
        if not isinstance(other, Process):
            return NotImplemented
        return (self.pid == other.pid and
                self.completion_time == other.completion_time and
                self.waiting_time == other.waiting_time)

# to allow processe to  used in sets and dictionary keys
    def __hash__(self):
        return hash((self.pid, self.arrival_time, self.burst_time, self.priority))
# uing it for future debugging 
    def __repr__(self):
        return (f"Process({self.pid},{self.arrival_time} , {self.burst_time}, {self.priority}, "
                f"completion_time={self.completion_time} , waiting_time={self.waiting_time})")
