import heapq
from collections import deque
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
        updated_proc = []
        waitingQ = []
        current_time = 0
        running = None
        process_index = 0
        processes_count = len(self.processes)
        finished_processes = 0

        while finished_processes < processes_count:
            # Add processes to the waiting queue as they arrive
            while process_index < processes_count and self.processes[process_index].arrival_time <= current_time:
                heapq.heappush(waitingQ, (self.processes[process_index].burst_time, self.processes[process_index]))
                process_index += 1

            # If no process is currently running, start the next one
            if not running and waitingQ:
                running = heapq.heappop(waitingQ)[1]

            if running:
                current_time += running.burst_time
                running.remaining_time = 0
                running.completion_time = current_time
                running.waiting_time = running.completion_time - running.arrival_time - running.burst_time
                updated_proc.append(running)
                finished_processes += 1
                running = None

            # Update waiting time for all processes in waiting queue
            for _, process in waitingQ:
                process.waiting_time += 1

        return updated_proc

    def srtf(self):
        updated_proc = []
        waitingQ = []
        current_time = 0
        running = None
        process_index = 0
        processes_count = len(self.processes)
        finished_processes = 0

        while finished_processes < processes_count:
            # Add processes to the waiting queue as they arrive
            while process_index < processes_count and self.processes[process_index].arrival_time <= current_time:
                heapq.heappush(waitingQ, (self.processes[process_index].remaining_time, self.processes[process_index]))
                process_index += 1

            # Check if the current running process needs to be preempted
            if running and waitingQ and waitingQ[0][0] < running.remaining_time:
                heapq.heappush(waitingQ, (running.remaining_time, running))
                running = heapq.heappop(waitingQ)[1]

            # If no process is currently running, start the next one
            if not running and waitingQ:
                running = heapq.heappop(waitingQ)[1]

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
            # Add processes to the waiting queue as they arrive
            while process_index < processes_count and self.processes[process_index].arrival_time <= current_time:
                waitingQ.append(self.processes[process_index])
                process_index += 1

            if waitingQ:
                current_process = waitingQ.popleft()
                exec_time = min(quantum, current_process.remaining_time)
                current_time += exec_time
                current_process.remaining_time -= exec_time

                # Add new arriving processes to the waiting queue
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
                else:
                    current_time += highest_priority_process.remaining_time
                    highest_priority_process.remaining_time = 0

                if highest_priority_process.remaining_time == 0:
                    highest_priority_process.completion_time = current_time
                    highest_priority_process.waiting_time = highest_priority_process.completion_time - highest_priority_process.arrival_time - highest_priority_process.burst_time
                    updated_proc.append(highest_priority_process)
                    finished_processes += 1
            else:
                current_time += 1

        return updated_proc if updated_proc else None
