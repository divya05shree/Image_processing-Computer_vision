import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("website.jpg")
cv2.imshow('original',image)


#ROTATE THE IMAGE
#CENTER THE IMAGE SHAPE BY DIVIDING WITH 2,ANGLE TO ROTATE IMG,SCALE SET TO 1 FOR ZOOMING
center=(image.shape[1]//2,image.shape[0]//2)
angle=180
scale=1
#USE getRotationMatrix2D AND GIVE PARAMTERS CENTER,ANGLE,SCALE
rotated_matrix=cv2.getRotationMatrix2D(center,angle,scale)
rotated_image=cv2.warpAffine(image,rotated_matrix,(image.shape[1],image.shape[0]))
#SUBPLOTS 1ROW ,2COLUMN
fig,axs=plt.subplots(1,2,figsize=(7,4))
axs[0].imshow(image)
axs[0].set_title('original_image')

axs[1].imshow(rotated_image)
axs[1].set_title('rotated_image')


for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()