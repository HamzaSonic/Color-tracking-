# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 16:44:04 2020

@author: Sonic
"""

import cv2
import imutils

cap =cv2.VideoCapture(0)
greenLower=(29,86,6)
greenUpper=(64,255,255)
while(True):
    ret, frame=cap.read()
    blurred =cv2.GaussianBlur(frame, (11,11), 0)
    hsv=cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    
    mask =cv2.inRange(hsv,greenLower,greenUpper) 
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)
    cnts =cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    if len(cnts)>0:
        c=max(cnts,key=cv2.contourArea)
        ((x,y),raduis)= cv2.minEnclosingCircle(c)
        cv2.circle(frame,(int(x),int(y)),int(raduis),(0,0,255),2)
        cv2.putText(frame, "location:({},{})".format(int(x),int(y)), (50,50), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
        
        
        
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()  

