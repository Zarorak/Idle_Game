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