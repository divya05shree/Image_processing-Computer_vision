import cv2
import numpy as np 
image=cv2.imread("website.jpg")
cv2.imshow('original',image)
cv2.waitKey(0) 
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale',gray_image)
cv2.waitKey(0) 
cv2.destroyAllWindows()