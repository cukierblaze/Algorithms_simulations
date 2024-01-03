
from processes import Process
import random
class Generator:
    @staticmethod
    def generator(num_processes,arrival_min,arrival_max,burst_min,burst_max):
        processes = []
        for i in range(num_processes):
            name = i+1
            arrival_time = random.randint(arrival_min, arrival_max)
            burst_time = random.randint(burst_min, burst_max)
            processes.append(Process(name, arrival_time, burst_time))
        return processes

