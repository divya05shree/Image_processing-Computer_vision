import cv2

image=cv2.imread('website.jpg')
cv2.imshow('Original_Image', image) 
b,g,r = cv2.split(image)
cv2.imshow("Model Blue Image", b) 
cv2.imshow("Model green Image", g)
cv2.imshow("Model red Image", r)
image_merge = cv2.merge([r, g, b]) 
cv2.imshow("Merged Image", image_merge)
cv2.waitKey(0)
cv2.destroyAllWindows()  
