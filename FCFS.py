from processes import Process

def FCFS(procesy):
    procesy=[proces1,proces2,proces3,proces4]
    procesy.sort(key=lambda x: x.arrival_time)
    for process in procesy:
        print(f"{process.name}:Arrival time={process.arrival_time},Burst time={process.burst_time}")
        #print(process.name)
    return procesy
if __name__ == "__main__":
    scheduled_processes = FCFS([proces1, proces2, proces3, proces4])
    proces1 = Process("a", 2, 3)
    proces2 = Process("b", 4, 9)
    proces3 = Process("c", 1, 1)
    proces4 = Process("d", 8, 2)


