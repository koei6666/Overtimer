from datetime import datetime

class Time:

    def __init__(self):
        self.startime = None
        self.endtime = None
    
    def timestamp(self,switch):
        timestamp = datetime.now().time()
        if switch:
            self.startime = timestamp
        else:
            self.endtime = timestamp

