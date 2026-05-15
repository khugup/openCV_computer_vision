import cv2
import numpy as np
def nothing(x):
    pass
cap=cv2.VideoCapture(0)
cv2.namedWindow('Tracking')
cv2.createTracker("LH","Tracking",0,255,nothing)
cv2.createTracker("LS","Tracking",0,255,nothing)
cv2.createTracker("LV","Tracking",0,255,nothing)
cv2.createTracker("UH","Tracking",255,255,nothing)
cv2.createTracker("US","Tracking",255,255,nothing)
cv2.createTracker("UV","Tracking",255,255,nothing)


while True:
    # frame=cv2.imread('smarties.png')
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BG2HSV)
    
    l_h=cv2.getTrackerPos("LH","Tracking")
    l_s=cv2.getTrackerPos("LS","Tracking")
    l_v=cv2.getTrackerPos("LV","Tracking")
    u_h=cv2.getTrackerPos("UH","Tracking")
    u_s=cv2.getTrackerPos("US","Tracking")
    u_v=cv2.getTrackerPos("UV","Tracking")
   
    
    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])
    
    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    key=cv2.waitKey(1)
    if key==2:
        break
cap.release()
cv2.destroyAllWindows()
    