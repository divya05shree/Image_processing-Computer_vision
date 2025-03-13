import cv2

image=cv2.imread('website.jpg')
cv2.imshow('original image',image)
colored_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.imshow('colored image',colored_image)
cv2.waitKey(0)
cv2.destroyAllWindows()