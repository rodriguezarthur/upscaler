import cv2
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import sys
import median_filter

#open the image
image = cv2.imread("Noise-Image.1.jpg")

#apply a median filter to reduce the noise
denoised_image = median_filter.medianfilter(image)

plt.imshow(denoised_image)
plt.show()
