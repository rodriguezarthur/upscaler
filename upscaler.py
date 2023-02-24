import cv2
import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import sys
import median_filter
import bicubic_interpolation
import bilinear_interpolation

#open the image
image_bgr = cv2.imread("./img/Noise-Image.1.jpg")
image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

#apply a median filter to reduce the noise
#denoised_image = median_filter.medianfilter(image)

#apply bilinear interpolation to upscale the image
#enlarged_image = bilinear_interpolation.enlarge_image(denoised_image,5)
upscaled_image = bilinear_interpolation.bilinear_interpolation(image,5)

fig, axs = plt.subplots(1,2, figsize=(10,5))

axs[0].imshow(image)
#axs[1].imshow(denoised_image)
axs[1].imshow(upscaled_image)

plt.show()
