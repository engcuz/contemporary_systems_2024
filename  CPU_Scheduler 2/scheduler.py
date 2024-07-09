# update July 5th today 11:40 PM
import heapq
from collections import deque
from process import Process

# Define   class cpu schedulre 
class Scheduler:
    # list of  process 
    def __init__(self, processes):
        self.processes = processes

# define rthe  fcfs method 
    def fcfs(self):
        current_time = 0
        # sort   process  by arreiva time 
        for process in sorted(self.processes, key=lambda x: x.arrival_time):
        # update current time if current time is < than  arrival time
            if current_time < process.arrival_time:
                current_time = process.arrival_time
            process.completion_time = current_time + process.burst_time
            process.waiting_time = current_time - process.arrival_time
            current_time += process.burst_time
        return self.processes

    def sjf(self):
        #List to store processes in  order it complete
        updated_proc = []
        waitingQ = []
        current_time = 0
        running = None
        process_index = 0
        processes_count = len(self.processes)
        finished_processes = 0

        while finished_processes < processes_count:
            # add processes to  waiting queue as it arrive
            while process_index < processes_count and self.processes[process_index].arrival_time <= current_time:
                heapq.heappush(waitingQ, (self.processes[process_index].burst_time, self.processes[process_index]))
                process_index += 1

            # If no process is running, start  next one
            if not running and waitingQ:
                running = heapq.heappop(waitingQ)[1]
#      # If process is running, continue until is complete.

            if running:
                current_time += running.burst_time
                running.remaining_time = 0
                running.completion_time = current_time
                running.waiting_time = running.completion_time - running.arrival_time - running.burst_time
                updated_proc.append(running)
                finished_processes += 1
                running = None

            # update waiting time for all processes in waiting queue, incremental
            for _, process in waitingQ:
                process.waiting_time += 1

        return updated_proc

# Shortest remaining time first scheduling algorithm
    def srtf(self):
        updated_proc = []
        waitingQ = []
        current_time = 0
        running = None
        process_index = 0
        processes_count = len(self.processes)
        finished_processes = 0
# xecute until all process is finished
        while finished_processes < processes_count:
            #enqueue process based on their remaining time/
            while process_index < processes_count and self.processes[process_index].arrival_time <= current_time:
                heapq.heappush(waitingQ, (self.processes[process_index].remaining_time, self.processes[process_index]))
                process_index += 1

            # check if  current running process need to be preempted
            if running and waitingQ and waitingQ[0][0] < running.remaining_time:
                heapq.heappush(waitingQ, (running.remaining_time, running))
                running = heapq.heappop(waitingQ)[1]

            # If no process is currently running, start  next one
            if not running and waitingQ:
                running = heapq.heappop(waitingQ)[1]
# execute  current process for one unit of time
            if running:
                running.remaining_time -= 1
                current_time += 1
                if running.remaining_time == 0:
                    running.completion_time = current_time
                    running.waiting_time = current_time - running.arrival_time - running.burst_time
                    updated_proc.append(running)
                    finished_processes += 1
                    running = None

            # Update waiting time for all processes in waiting queue
            for _, process in waitingQ:
                process.waiting_time += 1

        return updated_proc

    def rr(self, quantum):
        current_time = 0
        waitingQ = deque()
        updated_proc = []
        process_index = 0
        processes_count = len(self.processes)
        finished_processes = 0

        while finished_processes < processes_count:
            # add processes to  waiting queue as  arrive
            while process_index < processes_count and self.processes[process_index].arrival_time <= current_time:
                waitingQ.append(self.processes[process_index])
                process_index += 1
    #             # Process  first process in the queue.

            if waitingQ:
                current_process = waitingQ.popleft()
                exec_time = min(quantum, current_process.remaining_time)
                current_time += exec_time
                current_process.remaining_time -= exec_time

                # add new arriving processes to  waiting queue
                while process_index < processes_count and self.processes[process_index].arrival_time <= current_time:
                    waitingQ.append(self.processes[process_index])
                    process_index += 1

                if current_process.remaining_time == 0:
                    current_process.completion_time = current_time
                    current_process.waiting_time = current_process.completion_time - current_process.arrival_time - current_process.burst_time
                    updated_proc.append(current_process)
                    finished_processes += 1
                else:
                    waitingQ.append(current_process)
#                 # Update  waiting time for all processes in the queue.

                for process in waitingQ:
                    process.waiting_time += exec_time
            else:
                current_time += 1

        return updated_proc


# implements priority scheduling, / preemptive / none
    def priority(self, preemptive=False):
        updated_proc = []
        current_time = 0
        total_processes = len(self.processes)
        finished_processes = 0
        waitingQ = []
        in_heap = set()
# execute until all processes is finished
        while finished_processes < total_processes:
            #e nqueue processes based on  priority as they arrive
            for process in self.processes:
                if process.arrival_time <= current_time and process.remaining_time > 0 and process not in in_heap:
                    heapq.heappush(waitingQ, (process.priority, process.arrival_time, process))
                    in_heap.add(process)

            if waitingQ:
                _, _, highest_priority_process = heapq.heappop(waitingQ)
                in_heap.remove(highest_priority_process)

                if preemptive:
                    # Run for one unit of time / 
                    highest_priority_process.remaining_time -= 1
                    current_time += 1

                    if highest_priority_process.remaining_time == 0:
                        highest_priority_process.completion_time = current_time
                        highest_priority_process.waiting_time = highest_priority_process.completion_time - highest_priority_process.arrival_time - highest_priority_process.burst_time
                        updated_proc.append(highest_priority_process)
                        finished_processes += 1
                    else:
                        heapq.heappush(waitingQ, (highest_priority_process.priority, highest_priority_process.arrival_time, highest_priority_process))
                        in_heap.add(highest_priority_process)
                else:
                    # run to completion
                    current_time += highest_priority_process.remaining_time
                    highest_priority_process.remaining_time = 0
                    highest_priority_process.completion_time = current_time
                    highest_priority_process.waiting_time = highest_priority_process.completion_time - highest_priority_process.arrival_time - highest_priority_process.burst_time
                    updated_proc.append(highest_priority_process)
                    finished_processes += 1
            else:
                current_time += 1

        return updated_proc
    

    