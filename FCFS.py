from processes import Process


def FCFS(processes):

    not_done = len(processes)
    waiting_sum = 0
    time = 0
    queue = []
    executing = None
    burst = None

    # Simulating working processor
    while not_done > 0:

        # Checking whether any process arrived
        for process in processes:
            if process.arrival == time:

                # Adding to queue if occupied
                if executing:
                    queue.append(process)

                # If not occupied starts executing a new process
                else:
                    executing = process
                    burst = process.burst

        # Finishing a process when it's done
        if burst == 0:

            not_done -= 1
            executing.set_finish(time)
            waiting_sum += executing.waiting
            executing = None
            burst = None

            # If there are any processes in queue, starting to execute the first one
            if queue:
                executing = queue.pop(0)
                burst = executing.burst

        if burst:
            burst -= 1

        time += 1

    # Returning average time of waiting
    return waiting_sum/len(processes)

