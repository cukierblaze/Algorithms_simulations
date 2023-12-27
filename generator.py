
from processes import Process
import random
class Generator:
    def generator(self, num_processes,a,b,c,d):
        processes = []
        for i in range(num_processes):
            name = i+1
            arrival_time = random.randint(a, b)  # Adjust the range based on your requirements
            burst_time = random.randint(c, d)  # Adjust the range based on your requirements
            processes.append(Process(name, arrival_time, burst_time))
        return processes

