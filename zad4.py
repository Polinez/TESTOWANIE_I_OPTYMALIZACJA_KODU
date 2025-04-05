import cv2
import numpy as np
image = cv2.imread('pingwin.jpg')


added = cv2.add(image, np.array([10,-20,30]))

cv2.imshow('Original Image', image)
cv2.imshow('Added Image', added)

cv2.waitKey(0)