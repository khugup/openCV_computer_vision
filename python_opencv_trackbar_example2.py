import numpy as np
import cv2 as cv

def nothing(x):
    print(x)
    

img=cv.imread('lena.jpg')
cv.namedWindow('image')

cv.createTrackbar('cp','image',10,400,nothing)
switch='color/gray'
cv.createTrackbar(switch,'image',0,1,nothing)

while(1):
    img=cv.imshow('leno',img)
    pos=cv.getTrackbarPos('cp','image')
    font=cv2.FONT_HERSHEY_COMPLEX
    k=cv.waitKey(1) & OxFF
    cv.putText(img,str(pos),(50,150),font,4,(0,0,255))
    if k==27:
        break

    s=cv.getTrackbarPos('switch','image')
    if s==0:
        pass
    else:
        img=cv.cvtColor(img,cv.COLOR_BG2GRAY)
        
cv.destroyAllWindows()