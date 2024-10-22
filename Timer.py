from threading import Event, Thread
import time

class Timer:

    def __init__(self, intervalMs) -> None:
        self.IntervalMs = intervalMs/1000
        self.LastEvent = time.time()
        self.Event = Event()
        self.Thread = None
        self.Started = False

    def start(self):
        self.Started = True
        self.Thread = Thread(target=self.clock)
        self.Thread.start()

    def isFlagged(self)->bool :
        if (self.Event.is_set()):
            self.Event.clear()
            return True
        return False

    def stop(self):
        self.Started = False

    def clock(self):
        print("Clock started")
        
        while (self.Started):
            now = time.time()
            
            if (now - self.LastEvent > self.IntervalMs):
                self.Event.set()
                self.LastEvent = now
        print("Clock stopped")
        return
    
class TimedEvents:

    def __init__(self) -> None:
        self.CheckIntervalThread = None
        self.Started = False
        self.Intervals = {}
        
    def start(self):
        self.Started = True
        self.CheckIntervalThread = Thread(target=self.CheckIntervals)
        self.CheckIntervalThread.start()
    
    def stop(self):
        self.Started = False

    def AddEvent(self, intervalMs):
        newSingleEvent = SingleEvent()
        self.Intervals[intervalMs] = newSingleEvent
        return newSingleEvent

    def removeEvent(self, interval):
        self.Intervals.pop(interval)

    def CheckIntervals(self):
        while(self.Started):
            now = time.time()  
            for interval in self.Intervals:
                singleEvent = self.Intervals[interval]
                if now - singleEvent.LastEvent >= interval/1000:
                    singleEvent.Set(now)
                    

class SingleEvent:
    def __init__(self) -> None:
        self.LastEvent = time.time()
        self.Event = Event()

    def Set(self, now):
        self.Event.set()
        self.LastEvent = now

    def IsFlagged(self):
        if (self.Event.is_set()):
            self.Event.clear()
            return True
        return False
        