
class Process:
    def __init__(self,name,arrival_time,burst_time):
        self.name=name
        self.arrival_time=arrival_time
        self.burst_time=burst_time
        self.start_time=0
        self.finished = 0
        self.waiting=0
        self.turnaround=0
    def set_start(self,time):
        self.start_time = time
        self.finished =self.start_time+self.burst_time
        self.waiting=self.start_time-self.arrival_time


