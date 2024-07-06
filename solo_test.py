from scheduler import Scheduler
from process import Process

def test_sjf():
    # Define the processes
    processes = [
        Process(1, 0, 4, 2),
        Process(2, 2, 6, 1),
        Process(3, 4, 4, 3),
        Process(4, 6, 5, 2),
        Process(5, 10, 2, 1)
    ]

    # Expected results for SJF
    expected_results = {
        1: {"completion_time": 4, "waiting_time": 0},
        3: {"completion_time": 8, "waiting_time": 0},
        4: {"completion_time": 13, "waiting_time": 2},
        5: {"completion_time": 15, "waiting_time": 3},
        2: {"completion_time": 21, "waiting_time": 13}
    }

    

    # Initialize the scheduler with the processes
    scheduler = Scheduler(processes)

    # Run the SJF scheduling
    result = scheduler.sjf()
    result.sort(key=lambda x: x.pid)  # Sort results by PID

    # Output the results and validate
    print("SJF Results:")
    for process in result:
        print(f"PID: {process.pid}, Completion Time: {process.completion_time}, Waiting Time: {process.waiting_time}")
        assert process.completion_time == expected_results[process.pid]["completion_time"], f"Error in completion time for PID {process.pid}"
        assert process.waiting_time == expected_results[process.pid]["waiting_time"], f"Error in waiting time for PID {process.pid}"

    print("All assertions passed for SJF.")

if __name__ == "__main__":
    test_sjf()
