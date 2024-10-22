import time
import cv2
import numpy as np
from threading import Thread, Event
from Timer import Timer, TimedEvents

def main():
    previousTime = time.time()
    startTime = previousTime
    
    eventHandler = TimedEvents()
    updateFrameEvent = eventHandler.AddEvent(5)
    stopEvent = eventHandler.AddEvent(5000)

    eventHandler.start()

    while(True):
        now = time.time()
    
        othervalue = now - startTime
        if (updateFrameEvent.IsFlagged()):
            UpdateWindow(othervalue)

        if(stopEvent.IsFlagged()):
            print("Stopping program")
            eventHandler.stop()
            

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

if __name__ == "__main__":
    main()









