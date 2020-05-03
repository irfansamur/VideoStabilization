# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:47:02 2020

@author: Lenovo
"""

import cv2
from vidstab import VidStab

stabilizer = VidStab()
def show_webcam(mirror=False):
    cam = cv2.VideoCapture(1)

    while True:
        ret_val, img = cam.read()
     
        if img is not None:
            # Perform any pre-processing of frame before stabilization here
            pass
     
        # Pass frame to stabilizer even if frame is None
        # stabilized_frame will be an all black frame until iteration 30
        stabilized_frame = stabilizer.stabilize_frame(input_frame=img,
                                                       smoothing_window=30)
        if stabilized_frame is None:
            # There are no more frames available to stabilize
            print("aq")
     
        # Perform any post-processing of stabilized frame here
        pass
    
    
def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()
