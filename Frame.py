class Frame:
    def __init__(self,index=None):
        self.page = None
        self.index = 0
        self.last_used_time = -1

    def set_page(self, page, last_used_time):
        self.page = page
        self.last_used_time = last_used_time

    def set_change(self, last_used_time):
        self.last_used_time = last_used_time
