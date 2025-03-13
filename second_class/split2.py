import cv2
import numpy as np
import matplotlib.pyplot as plt
def getQudrent(image):
    
    height, width = image.shape[:2]

    
    top_left = image[0:height//2, 0:width//2] 
    top_right = image[0:height//2, width//2:width] 
    bottom_left = image[height//2:height, 0:width//2]  
    bottom_right = image[height//2:height, width//2:width]  
    images = [top_left , top_right , bottom_left , bottom_right]
    count = len(images)
   
    for i in range(count):
        plt.subplot(2, 2, i + 1)
        plt.imshow(images[i])
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ =="__main__":
    image = cv2.imread("website.jpg")
    getQudrent(image)
# image_lined = cv2.line(image, , end_point, color, thickness)