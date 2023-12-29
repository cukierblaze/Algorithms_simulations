from processes import Process
from generator import Generator
def FCFS(processes):
    queue=[]
    occupied =False
    executed_processes=[]
    burst = None

    for time in range(0, sum(p.burst_time + p.arrival_time for p in processes) + 1):
        for proc in processes:
            if proc.arrival_time == time and proc not in executed_processes:
                if not occupied:
                    executed_processes.append(proc)
                    occupied = True
                    burst = proc.burst_time
                    print(f"Process {proc.name} executed at time {time}")
                else:
                    queue.append(proc)
        if burst == 0:
            if queue:
                burst = queue[0].burst_time
                print(f"Process {queue[0].name} executed at time {time}")
                executed_processes.append(queue.pop(0))
            else:
                occupied = False
        if burst:
            burst -= 1
    return executed_processes

""""
if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    a = int(input("Enter the lowest border of arrival_time: "))
    b = int(input("Enter the highest border of arrival_time: "))
    c = int(input("Enter the lowest border of burst_time: "))
    d = int(input("Enter the highest border of burst_time: "))

        # Ensure the upper bound is greater than or equal to the lower bound for both arrival_time and burst_time
    while b < a or d < c:
        print("Invalid input. Please make sure the upper bound is greater than or equal to the lower bound.")
        a = int(input("Enter the lowest border of arrival_time: "))
        b = int(input("Enter the highest border of arrival_time: "))
        c = int(input("Enter the lowest border of burst_time: "))
        d = int(input("Enter the highest border of burst_time: "))

    generator_instance = Generator()
    processes_to_schedule = generator_instance.generator(num_processes,a,b,c,d)

    scheduled_processes = FCFS(processes_to_schedule)
"""
FCFS([Process('a', 1, 4), Process('b', 1, 3), Process('c', 3, 2)])