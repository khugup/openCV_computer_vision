import numpy as np
import cv2
img=cv2.imread('leno.jpg')
print(img.shape) # returns a tuple of number of rows,columns and channels
print(img.size) # returns total number of pixels is accessed
print(img.dtype)# returns image datatype is obtained
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))


# copy ball to another end
ball=img[280:330,330:390]
img[273:333,100:160]=ball

cv2.imshow('leno.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



#  to add two images
import cv2
img=cv2.imread('leno.jpg')
img2=cv2.imread('messi.jpg')
print(img.shape) # returns a tuple of number of rows,columns and channels
print(img.size) # returns total number of pixels is accessed
print(img.dtype)# returns image datatype is obtained
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))


# copy ball to another end
ball=img[280:330,330:390]
img[273:333,100:160]=ball

img=cv2.resize(img,(512,512))
img=cv2.resize(img2,(512,512))
dst=cv2.addWeighted(img,.5,img2,.8,0)
cv2.imshow('leno.jpg',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

