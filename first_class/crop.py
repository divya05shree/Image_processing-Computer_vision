import cv2

image=cv2.imread('website.jpg')
cropped_image = image[80:280, 150:330]
cv2.imshow('original image',cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()