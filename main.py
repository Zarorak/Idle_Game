import time
import cv2
import numpy as np
from threading import Thread, Event

def main():
    previousTime = time.time()
    startTime = previousTime

    showWindowTimer = Timer(5)
    showWindowTimer.start()
    terminateTimer = Timer(5000)
    terminateTimer.start()

    while(True):
        now = time.time()
    
        othervalue = now - startTime
        if (showWindowTimer.isFlagged()):
            UpdateWindow(othervalue)

        if(terminateTimer.isFlagged()):
            print("Stopping program")
            showWindowTimer.stop()
            terminateTimer.stop()

def UpdateWindow(otherval):

    height, width = 400 ,1000

    window = np.zeros([height,width,3])
   
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (200,200)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    window = cv2.putText(window, str(otherval) , org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("main", window)
    cv2.waitKey(1)
    

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

if __name__ == "__main__":
    main()









