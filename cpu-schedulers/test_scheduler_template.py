#moved 
import pytest
from process import Process
from scheduler import Scheduler
from metrics import average_turnaround_time, average_waiting_time, cpu_utilization

# Sample processes for testing
sample_processes = [
    Process(1, 0, 4, 2),
    Process(2, 2, 6, 1),
    Process(3, 4, 4, 3),
    Process(4, 6, 5, 2),
    Process(5, 10, 2, 1)
]

# Example expected outputs for different scheduling algorithms
expected_fcfs = [
    Process(1, 0, 4, 2, completion_time=4, waiting_time=0),
    Process(2, 2, 6, 1, completion_time=10, waiting_time=2),
    Process(3, 4, 4, 3, completion_time=14, waiting_time=6),
    Process(4, 6, 5, 2, completion_time=19, waiting_time=8),
    Process(5, 10, 2, 1, completion_time=21, waiting_time=9)
]

expected_sjf = [
    Process(1, 0, 4, 2, completion_time=4, waiting_time=0),
    Process(3, 4, 4, 3, completion_time=8, waiting_time=0),
    Process(4, 6, 5, 2, completion_time=13, waiting_time=2),
    Process(5, 10, 2, 1, completion_time=15, waiting_time=3),
    Process(2, 2, 6, 1, completion_time=21, waiting_time=13)
]

expected_srtf = [
    Process(1, 0, 4, 2, completion_time=4, waiting_time=0),
    Process(3, 4, 4, 3, completion_time=8, waiting_time=0),
    Process(5, 10, 2, 1, completion_time=12, waiting_time=0),
    Process(4, 6, 5, 2, completion_time=15, waiting_time=4),
    Process(2, 2, 6, 1, completion_time=21, waiting_time=13)
]

expected_rr = [
    Process(1, 0, 4, 2, completion_time=6, waiting_time=2),
    Process(3, 4, 4, 3, completion_time=14, waiting_time=6),
    Process(5, 10, 2, 1, completion_time=16, waiting_time=4),
    Process(2, 2, 6, 1, completion_time=18, waiting_time=10),
    Process(4, 6, 5, 2, completion_time=21, waiting_time=10)
]

# Process 1 - Completion Time: 6, Waiting Time: 2
# Process 3 - Completion Time: 14, Waiting Time: 6
# Process 5 - Completion Time: 16, Waiting Time: 4
# Process 2 - Completion Time: 18, Waiting Time: 10
# Process 4 - Completion Time: 21, Waiting Time: 10


expected_priority_preemptive = [
    Process(2, 2, 6, 1, completion_time=8, waiting_time=0),
    Process(1, 0, 4, 2, completion_time=10, waiting_time=6),
    Process(5, 10, 2, 1, completion_time=12, waiting_time=0),
    Process(4, 6, 5, 2, completion_time=17, waiting_time=6),
    Process(3, 4, 4, 3, completion_time=21, waiting_time=13)
]

expected_priority_non_preemptive = [
    Process(1, 0, 4, 2, completion_time=4, waiting_time=0),
    Process(2, 2, 6, 1, completion_time=10, waiting_time=2),
    Process(5, 10, 2, 1, completion_time=12, waiting_time=0),
    Process(4, 6, 5, 2, completion_time=17, waiting_time=6),
    Process(3, 4, 4, 3, completion_time=21, waiting_time=13)
]

class TestCPUScheduler:
    @pytest.fixture(scope="class")
    def scheduler(self):
        return Scheduler(sample_processes)

    def test_process_class(self):
        process = Process(1, 0, 10, 3)
        assert process.pid == 1
        assert process.arrival_time == 0
        assert process.burst_time == 10
        assert process.priority == 3
        assert process.remaining_time == 10
        assert process.completion_time is None
        assert process.waiting_time == 0

    def test_fcfs(self, scheduler):
        result = scheduler.fcfs()
        assert result == expected_fcfs

    def test_sjf(self, scheduler):
        result = scheduler.sjf()
        assert result == expected_sjf
#d
    def test_rr(self, scheduler):
        result = scheduler.rr(quantum=2)
        assert result == expected_rr
#done
    def test_priority_non_preemptive(self, scheduler):
        result = scheduler.priority(preemptive=False)
        assert result == expected_priority_non_preemptive
#Done
    def test_priority_preemptive(self, scheduler):
        result = scheduler.priority(preemptive=True)
        assert result == expected_priority_preemptive
    
#Done
    def test_srtf(self, scheduler):
        result = scheduler.srtf()
        assert result == expected_srtf

    

    

    

    def test_metrics(self):
        att = average_turnaround_time(expected_fcfs)
        awt = average_waiting_time(expected_fcfs)
        cu = cpu_utilization(expected_fcfs)
        assert isinstance(att, float)
        assert isinstance(awt, float)
        assert isinstance(cu, float)
        assert 0 <= cu <= 100

    def test_edge_cases(self, scheduler):
        # Test edge cases for your scheduling algorithms
        pass

if __name__ == "__main__":
    pytest.main([__file__])
