import cv2

image=cv2.imread('website.jpg')
alpha=5
beta=5

adjusted=cv2.convertScaleAbs(image,alpha=alpha,beta=beta)
cv2.imshow('adjsuted image',adjusted)
cv2.waitKey()
cv2.destroyAllWindows()