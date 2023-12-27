
class Process:
    def __init__(self,name,arrival_time,burst_time):
        self.name=name
        self.arrival_time=arrival_time
        self.burst_time=burst_time
        self.start_time=0
        self.finished=0
