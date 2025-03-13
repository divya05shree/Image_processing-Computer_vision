import cv2

image=cv2.imread('website.jpg')
cv2.imshow("original",image)

image_bordered = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_CONSTANT,value = [10,10,10]) 
cv2.imshow('border image',image_bordered)
cv2.waitKey(0)
cv2.destroyAllWindows()