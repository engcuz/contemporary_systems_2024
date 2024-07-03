# Start July 2024

import heapq

from process import Process, ProcessByBurstTime, ProcessByRemainingTime
class Scheduler:
    def __init__(self, processes):
        self.processes = processes

    def fcfs(self):
        updated_proc = []
        running = 0
        wiating = []
        current_time = 0

        while running < len(self.processes):
            current_time += 1
            self.processes[running].remaining_time -= 1
            if self.processes[running].remaining_time == 0:
                self.processes[running].completion_time = current_time
                updated_proc.append(self.processes[running])
                running += 1

                if len(wiating) != 0:
                    wiating.pop(0)

            for i in self.processes:
                if i.arrival_time == current_time:
                    wiating.append(i)

            for j in wiating:
                j.waiting_time += 1


        return updated_proc

    # def sjf(self):
    #     updated_proc = []
    #     running = 0
    #     waitingQ = []
    #     current_time = 0
    #
    #     while running < len(self.processes):
    #         current_time += 1
    #         self.processes[running].remaining_time -= 1
    #         for i in range(running, len(self.processes)):
    #             if self.processes[i] <= current_time:
    #
    #         if self.processes[running].remaining_time == 0:
    #             self.processes[running].completion_time = current_time
    #             updated_proc.append(self.processes[running])
    #             running += 1

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
                heapq.heappush(waitingQ, self.processes[process_index])
                process_index += 1

            # If no process is currently running and there are processes in the waiting queue, start the next one
            if running is None and waitingQ:
                running = heapq.heappop(waitingQ)

            if running is not None:
                running.remaining_time -= 1
                if running.remaining_time == 0:
                    running.completion_time = current_time + 1
                    updated_proc.append(running)
                    finished_processes += 1
                    running = None  # No process is running now

            # Update waiting time for all processes in waiting queue
            for process in waitingQ:
                process.waiting_time += 1

            current_time += 1

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
                heapq.heappush(waitingQ, self.processes[process_index])
                process_index += 1

            # Check if the current running process needs to be preempted
            if running and waitingQ and waitingQ[0].remaining_time < running.remaining_time:
                heapq.heappush(waitingQ, running)
                running = heapq.heappop(waitingQ)

            # If no process is currently running, start the next one
            if running is None and waitingQ:
                running = heapq.heappop(waitingQ)

            if running is not None:
                running.remaining_time -= 1
                if running.remaining_time == 0:
                    running.completion_time = current_time + 1
                    updated_proc.append(running)
                    finished_processes += 1
                    running = None  # No process is running now

            # Update waiting time for all processes in waiting queue
            for process in waitingQ:
                process.waiting_time += 1

            current_time += 1

        return updated_proc

    def rr(self, quantum):
        current_time = 0
        waitingQ = []
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
                # Get the first process in the waiting queue
                current_process = waitingQ.pop(0)
                # Calculate the execution time for this process
                exec_time = min(quantum, current_process.remaining_time)
                # Update current time by the execution time
                current_time += exec_time
                # Reduce the remaining time of the current process
                current_process.remaining_time -= exec_time

                # If the process is finished
                if current_process.remaining_time == 0:
                    current_process.completion_time = current_time
                    updated_proc.append(current_process)
                    finished_processes += 1
                else:
                    # If the process is not finished, put it back in the waiting queue
                    waitingQ.append(current_process)

                # Update waiting time for all processes in waiting queue
                for process in waitingQ:
                    process.waiting_time += exec_time
            else:
                current_time += 1  # If no processes are ready, increment the current time

        return updated_proc

    def priority(self, preemptive=False):
        updated_proc = []
        current_time = 0
        total_processes = len(self.processes)
        finished_processes = 0

        while finished_processes < total_processes:
            # Find the process with the highest priority that has arrived
            highest_priority_process = None
            for process in self.processes:
                if process.arrival_time <= current_time and process.remaining_time > 0:
                    if highest_priority_process is None or process.priority < highest_priority_process.priority:
                        highest_priority_process = process

            if highest_priority_process:
                if preemptive:
                    # For preemptive priority scheduling, execute one time unit
                    highest_priority_process.remaining_time -= 1
                    current_time += 1
                else:
                    # For non-preemptive priority scheduling, execute until completion
                    current_time += highest_priority_process.remaining_time
                    highest_priority_process.remaining_time = 0

                if highest_priority_process.remaining_time == 0:
                    highest_priority_process.completion_time = current_time
                    updated_proc.append(highest_priority_process)
                    finished_processes += 1

                    # Calculate waiting time
                    highest_priority_process.waiting_time = highest_priority_process.completion_time - highest_priority_process.arrival_time - highest_priority_process.burst_time
            else:
                current_time += 1

        return updated_proc if updated_proc else None  # Return None if no processes were updated
