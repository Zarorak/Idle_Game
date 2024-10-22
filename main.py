import time
from datetime import datetime
import cv2
import numpy as np


windowName = "main"
lastWindowUpDate = time.time()
updateWindowEveryMs = 500

def main():

    incPerSec = 1.1
    multiplierPerSec = 1.0002
    value = 0
    previousTime = time.time()
    startTime = previousTime

    while(True):
        now = time.time()
        deltaTime = now - previousTime
        othervalue = now - startTime
        
        value += deltaTime 


        if ((now - lastWindowUpDate)*1000 >= updateWindowEveryMs):
            UpdateWindow(value, othervalue)

def UpdateWindow(newValue, otherval):

    height, width = 400 ,1000

    window = np.zeros([height,width,3])
   

    # font
    font = cv2.FONT_HERSHEY_SIMPLEX

    # org
    org = (200, 100)
    org2 = (200,200)
    # fontScale
    fontScale = 1
    
    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2
    
    # Using cv2.putText() method
    window = cv2.putText(window, str(newValue/1000) , org, font, 
                    fontScale, color, thickness, cv2.LINE_AA)
    window = cv2.putText(window, str(otherval) , org2, font, 
                    fontScale, color, thickness, cv2.LINE_AA)
    

    cv2.imshow(windowName, window)
    cv2.waitKey(2)
    lastWindowUpDate = time.time()
    return



if __name__ == "__main__":
    main()









