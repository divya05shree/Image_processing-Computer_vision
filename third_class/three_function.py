import cv2
import numpy as np 
import matplotlib.pyplot as plt
image=cv2.imread("website.jpg")
cv2.imshow('original',image)

#------------------------------------------------------------------------------------------
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

#scaling------------------------------------------------------------------------------------------------
#ORIJINAL IMG IS MULTIPLIED WITH VALUES FX=5,FY=5
half=cv2.resize(image,(0,0),fx=5,fy=5)
bigger=cv2.resize(image,(1024,1610))
stretch_near=cv2.resize(image,(780,540),interpolation=cv2.INTER_LINEAR)
Titles =["Oxriginal", "Half", "Bigger", "Interpolation Nearest"]
images =[image, half, bigger, stretch_near]
count = 4
for i in range(count):
    plt.subplot(3, 3, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])


#translation-----------------------
img = cv2.imread('website.jpg')

image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
width = image_rgb.shape[1]
height = image_rgb.shape[0]
#
tx = 250
ty = 250


translation_matrix = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)

translated_image = cv2.warpAffine(image_rgb, translation_matrix, (width, height))


fig, axs = plt.subplots(1, 2, figsize=(7, 4))


axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')


axs[1].imshow(translated_image)
axs[1].set_title('Image Translation')


for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

plt.tight_layout()
plt.show()
#-------------------------
cv2.waitKey(0) 
cv2.destroyAllWindows()