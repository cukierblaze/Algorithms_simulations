from processes import Process
def FCFS (procesy):
    #procesy.sort(key=lambda x:x.arrival_time)
    queue=[]
    current_time=0
    executed_process=[]

    while procesy or queue:
        if current_time == procesy.arrival_time:

            queue.append(procesy.arrival_time)
            current_proccess= procesy[queue]
            print(f"Proces {current_proccess} czas {current_proccess.burst_time}")
            procesy.pop()
            current_time+=current_time.burst_time
        if procesy.arrival_time < current_time:
            queue.append(procesy.arrival_time)
