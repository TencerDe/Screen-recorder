import cv2
import numpy as np
import pyautogui
from win32api import GetSystemMetrics
import time
 
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

dimension = (width, height)

format = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("test.mp4",format,30.0,dimension)

time_cr = time.time()

duration = 15+4

time_end = time_cr + duration

while True:
    img = pyautogui.screenshot()
    frame_1 = np.array(img)
    frame = cv2.cvtColor(frame_1,cv2.COLOR_BGR2RGB)

    output.write(frame)

    c_time = time.time()

    if c_time > time_end:
        break

output.release()
print("____END____")

