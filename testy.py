from FCFS import FCFS
from SJF import SJF
import time
from generator import Generator
from processes import Process
def run_algorithm(algorithm, processes,output_file):
    start_time = time.time()
    scheduled_processes = algorithm(processes)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Total execution time: {execution_time:.6f} seconds\n")
    with open(output_file, 'a') as file:
        file.write(f"Number of processes: {len(processes)}\n")
        file.write(f"Algorithm: {algorithm.__name__}\n")
        file.write(f"Total execution time: {execution_time:.6f} seconds\n\n")

if __name__=="__main__":
    output_file = "algorithm_results.txt"
    for i in range(1,100,10):
        num_processes = i #int(input("Enter the number of processes: "))  # Specify the number of processes to generate
        generator_instance = Generator()
        processes_to_schedule = generator_instance.generator(num_processes,1,1000,1,20)

    proces1=Process("a",22,15)
    proces2=Process("b",7,4)
    proces3=Process("c",34,8)
    proces4=Process("d",6,9)
    proces5=Process("e",28,15)
    proces6=Process("f",90,104)
    scheduled_process=FCFS([proces1,proces2,proces3,proces4,proces5,proces6])

    proces1 = Process("a", 22, 15)
    proces2 = Process("b", 7, 4)
    proces3 = Process("c", 34, 8)
    proces4 = Process("d", 6, 9)
    proces5 = Process("e", 28, 15)
    proces6 = Process("f", 90, 104)
    scheduled_process = SJF([proces1, proces2, proces3, proces4, proces5, proces6])

