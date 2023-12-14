from processes import Process

def SJF(processes):
    queue=[]
    occupied =False
    executed_processes=[]

    for time in range(1,sum(p.burst_time + p.arrival_time for p in processes) + 1):
        for proc in processes:
            if proc.arrival_time <= time and proc not in executed_processes:
                if not occupied:
                    executed_processes.append(proc)
                    occupied = True
                    print(f"Process {proc.name} executed at time {time}")
                else:
                    queue.append(proc)
        if queue:
            processes.sort(lambda x: x.burst_time)
            next_proccess = queue.pop(0)
            executed_processes.append(next_proccess)
            occupied=True
            print(f"Process {proc.name} executed at time {time}")
        occupied=False
    return executed_processes


if __name__ == "__main__":
    proces1 = Process("a", 1, 3)
    proces2 = Process("b", 5, 9)
    proces3 = Process("c", 4, 1)
    proces4 = Process("d", 9, 2)
    scheduled_processes = SJF([proces1, proces2, proces3, proces4])

