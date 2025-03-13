import cv2
from matplotlib import pyplot as plt
import numpy as np

def enhancement(img, brightness=10, contrast=2.3):
    image2 = cv2.addWeighted(img, contrast, np.zeros(img.shape, img.dtype), 0, brightness)
    return image2

def low_contrast_segmentation(img, threshold=30):
    _, segmented_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), threshold, 255, cv2.THRESH_BINARY)
    return segmented_img

# Read the input colored image
img = cv2.imread('nature.png')


# Segment the low contrast areas
segmented_img = low_contrast_segmentation(img, threshold=30)


# Create a figure to display the images and plots
plt.figure(figsize=(18, 6))

# Display the original image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')


# Display the segmented image
plt.subplot(1, 3, 3)
plt.imshow(segmented_img, cmap='gray')
plt.title('Segmented Low Contrast Areas')
plt.axis('off')




# Show the combined plots
plt.show()
