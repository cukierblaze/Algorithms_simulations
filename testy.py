import sys

# Save the standard output to a variable
original_stdout = sys.stdout

# Open a file in write mode to save the output
with open('output.txt', 'w') as f:
    # Redirect the standard output to the file
    sys.stdout = f
    from FCFS import FCFS
    from SJF import SJF
    import time
    from generator import Generator
    from processes import Process

    print("\n 5 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(5,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 10 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(10,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 20 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(20,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 50 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(50,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 100 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(100,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)
    print("\n--------------------------------------------------------------------------------------------\n")
    print("\n 5 processes, Arrival time from 0 to 100, Burst time:5\n")
    test=Generator.generator(5,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 10 processes, Arrival time from 0 to 100, Burst time :5\n")
    test=Generator.generator(10,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 20 processes, Arrival time from 0 to 100, Burst time:5\n")
    test=Generator.generator(20,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 50 processes, Arrival time from 0 to 100, Burst time:5\n")
    test=Generator.generator(50,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 100 processes, Arrival time from 0 to 100, Burst time: 5\n")
    test=Generator.generator(100,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)
    print("\n------------------------------------------------------------------------------------\n")
    print("\n 5 processes, Arrival time:0, Burst time form 1 to 10\n")
    test=Generator.generator(5,0,0,1,10)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 10 processes, Arrival time:0, Burst time from 1 to 10\n")
    test=Generator.generator(10,0,0,1,10)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 20 processes, Arrival time:0, Burst time from 1 to 10\n")
    test=Generator.generator(20,0,0,1,10)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 50 processes, Arrival time:0, Burst time from 1 to 10\n")
    test=Generator.generator(50,0,0,1,10)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 100 processes, Arrival time:0, Burst time from 1 to 10\n")
    test=Generator.generator(100,0,0,1,10)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    FCFS(test)

    print("\n 100 processes, Arrival time from 0 to 100, Burst time: 10\n")
    test=Generator.generator(100,0,0,10,10)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)
    from FCFS import FCFS
    from SJF import SJF
    import time
    from generator import Generator
    from processes import Process

    print("\n 5 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(5,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 10 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(10,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 20 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(20,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 50 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(50,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 100 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(100,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)
    print("\n--------------------------------------------------------------------------------------------\n")
    print("\n 5 processes, Arrival time from 0 to 100, Burst time:5\n")
    test=Generator.generator(5,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 10 processes, Arrival time from 0 to 100, Burst time :5\n")
    test=Generator.generator(10,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 20 processes, Arrival time from 0 to 100, Burst time:5\n")
    test=Generator.generator(20,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 50 processes, Arrival time from 0 to 100, Burst time:5\n")
    test=Generator.generator(50,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 100 processes, Arrival time from 0 to 100, Burst time: 5\n")
    test=Generator.generator(100,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)
    print("\n------------------------------------------------------------------------------------\n")
    print("\n 5 processes, Arrival time:0, Burst time form 1 to 10\n")
    test=Generator.generator(5,0,0,1,10)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 10 processes, Arrival time:0, Burst time from 1 to 10\n")
    test=Generator.generator(10,0,0,1,10)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 20 processes, Arrival time:0, Burst time from 1 to 10\n")
    test=Generator.generator(20,0,0,1,10)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 50 processes, Arrival time:0, Burst time from 1 to 10\n")
    test=Generator.generator(50,0,0,1,10)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 100 processes, Arrival time:0, Burst time from 1 to 10\n")
    test=Generator.generator(100,0,0,1,10)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)


    print("\n 100 processes, Arrival time from 0 to 100, Burst time: 10\n")
    test=Generator.generator(100,0,0,10,10)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)
    from FCFS import FCFS
    from SJF import SJF
    import time
    from generator import Generator
    from processes import Process

    print("\n 5 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(5,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 10 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(10,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 20 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(20,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 50 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(50,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 100 processes, Arrival time from 0 to 100, Burst time from 1 to 5\n")
    test=Generator.generator(100,0,100,1,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)
    print("\n--------------------------------------------------------------------------------------------\n")
    print("\n 5 processes, Arrival time from 0 to 100, Burst time:5\n")
    test=Generator.generator(5,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 10 processes, Arrival time from 0 to 100, Burst time :5\n")
    test=Generator.generator(10,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 20 processes, Arrival time from 0 to 100, Burst time:5\n")
    test=Generator.generator(20,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 50 processes, Arrival time from 0 to 100, Burst time:5\n")
    test=Generator.generator(50,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)

    print("\n 100 processes, Arrival time from 0 to 100, Burst time: 5\n")
    test=Generator.generator(100,0,100,5,5)
    print("\nSJF:")
    SJF(test)
    print("\nFCFS: ")
    FCFS(test)
sys.stdout = original_stdout