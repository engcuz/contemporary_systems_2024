import pytest
from process import Process
from scheduler import Scheduler
from metrics import average_turnaround_time, average_waiting_time, cpu_utilization

'''
Note: This is a template for the test file. Do not change the imports or function names!!!
If imports are not working, make sure this file is in the same directory as your other files,
and that all classes and functions are named correctly.
'''

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

# Add more expected outputs for other algorithms as needed...

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
        # result = scheduler.sjf()
        # assert result == expected_sjf
        pass

    def test_srtf(self, scheduler):
        # result = scheduler.srtf()
        # assert result == expected_srtf
        pass

    def test_rr(self, scheduler):
        # result = scheduler.rr(quantum=2)
        # assert result == expected_rr
        pass

    def test_priority(self, scheduler):
        # result = scheduler.priority()
        # assert result == expected_priority
        pass

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
