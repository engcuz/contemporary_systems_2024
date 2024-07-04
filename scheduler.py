# scheduler.py
from collections import deque
import heapq
from process import Process

class Scheduler:
    def __init__(self, processes):
        self.processes = processes

    def fcfs(self):
        current_time = 0
        for process in sorted(self.processes, key=lambda x: x.arrival_time):
            if current_time < process.arrival_time:
                current_time = process.arrival_time
            process.completion_time = current_time + process.burst_time
            process.waiting_time = current_time - process.arrival_time
            current_time += process.burst_time
        return self.processes

    def sjf(self):
        processes = sorted(self.processes, key=lambda x: x.arrival_time)
        current_time = 0
        completed_processes = []
        ready_queue = []
        while processes or ready_queue:
            while processes and processes[0].arrival_time <= current_time:
                heapq.heappush(ready_queue, processes.pop(0))
            if not ready_queue:
                current_time = processes[0].arrival_time
                continue
            process = heapq.heappop(ready_queue)
            if current_time < process.arrival_time:
                current_time = process.arrival_time
            process.completion_time = current_time + process.burst_time
            process.waiting_time = current_time - process.arrival_time
            current_time += process.burst_time
            completed_processes.append(process)
        return completed_processes



######
    def srtf(self):
        processes = sorted(self.processes, key=lambda x: x.arrival_time)
        current_time = 0
        completed_processes = []
        ready_queue = []
        while processes or ready_queue:
            while processes and processes[0].arrival_time <= current_time:
                heapq.heappush(ready_queue, (processes[0].remaining_time, processes.pop(0)))
            if not ready_queue:
                current_time = processes[0].arrival_time
                continue
            remaining_time, process = heapq.heappop(ready_queue)
            current_time += 1
            process.remaining_time -= 1
            if process.remaining_time == 0:
                process.completion_time = current_time
                process.waiting_time = current_time - process.arrival_time - process.burst_time
                completed_processes.append(process)
            else:
                heapq.heappush(ready_queue, (process.remaining_time, process))
        return completed_processes


# ----------
    def rr(self, quantum):
        current_time = 0
        waitingQ = deque()
        updated_proc = []
        process_index = 0
        processes_count = len(self.processes)
        finished_processes = 0

        while finished_processes < processes_count:
            while process_index < processes_count and self.processes[process_index].arrival_time <= current_time:
                waitingQ.append(self.processes[process_index])
                process_index += 1

            if waitingQ:
                current_process = waitingQ.popleft()
                exec_time = min(quantum, current_process.remaining_time)
                current_time += exec_time
                current_process.remaining_time -= exec_time

                if current_process.remaining_time == 0:
                    current_process.completion_time = current_time
                    updated_proc.append(current_process)
                    finished_processes += 1
                else:
                    waitingQ.append(current_process)

                for process in waitingQ:
                    process.waiting_time += exec_time
            else:
                current_time += 1

        return updated_proc

    def priority(self, preemptive=False):
        updated_proc = []
        current_time = 0
        total_processes = len(self.processes)
        finished_processes = 0

        while finished_processes < total_processes:
            highest_priority_process = None
            for process in self.processes:
                if process.arrival_time <= current_time and process.remaining_time > 0:
                    if highest_priority_process is None or process.priority < highest_priority_process.priority:
                        highest_priority_process = process

            if highest_priority_process:
                if preemptive:
                    highest_priority_process.remaining_time -= 1
                    current_time += 1

                    if highest_priority_process.remaining_time == 0:
                        highest_priority_process.completion_time = current_time
                        highest_priority_process.waiting_time = highest_priority_process.completion_time - highest_priority_process.arrival_time - highest_priority_process.burst_time
                        updated_proc.append(highest_priority_process)
                        finished_processes += 1
                else:
                    current_time += highest_priority_process.remaining_time
                    highest_priority_process.remaining_time = 0
                    highest_priority_process.completion_time = current_time
                    highest_priority_process.waiting_time = highest_priority_process.completion_time - highest_priority_process.arrival_time - highest_priority_process.burst_time
                    updated_proc.append(highest_priority_process)
                    finished_processes += 1
            else:
                current_time += 1

        return updated_proc if updated_proc else None
