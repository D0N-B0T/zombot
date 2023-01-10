import cv2
import numpy as np
import os
from time import time
import win32gui, win32ui, win32con, win32api
from windowcapture import WindowCapture
from vision import Vision



# WindowCapture.list_window_names()
# exit()

wincap = WindowCapture('Steam')

ladybug_mob = Vision('img2/ladybug.png')

loop_time = time()



while(True):   
    screenshot = wincap.get_screenshot()
    
    points = ladybug_mob.find(screenshot, 0.8, 'rectangles')
    #cv2.imshow('Florr.io Bot', screenshot)   
    
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break


print('done')
