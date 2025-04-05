import cv2
import numpy as np
image = cv2.imread('pingwin.jpg')

M= np.ones(image.shape, dtype="uint8") +80
added = cv2.subtract(image, M)

cv2.imshow('Original Image', image)
cv2.imshow('Added Image', added)

addedNP = image - M

cv2.imshow('Added Image with Numpy', addedNP)

print("Miejsca gdzie w numbp byly czarne zamieniaja sie na biale a w cv2 zostaja czarne ")
cv2.waitKey(0)