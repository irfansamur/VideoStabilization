# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:49:17 2020

@author: Lenovo
"""

import time
import cv2
from vidstab import VidStab

stabilizer = VidStab()
vidcap = cv2.VideoCapture(0)

start_time = time.time()
x = 1 # displays the frame rate every 1 second
counter = 0

while True:
     grabbed_frame, frame = vidcap.read()
     if frame is not None:
        pass
     
     stabilized_frame = stabilizer.stabilize_frame(input_frame=frame,smoothing_window=5)
     img = cv2.putText(stabilized_frame,str(counter / (time.time() - start_time)),(20,30),cv2.FONT_HERSHEY_COMPLEX,1.2,(0,0,255),2)
     if stabilized_frame is None:
         break
     
     cv2.imshow('Test',stabilized_frame)
     counter+=1
     if (time.time() - start_time) > x :
        print("FPS: ", counter / (time.time() - start_time))
        counter = 0
        start_time = time.time()

     if cv2.waitKey(1) & 0xFF == ord('q'):
         break