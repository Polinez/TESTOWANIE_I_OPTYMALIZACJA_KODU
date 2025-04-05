import cv2
import numpy as np
image = cv2.imread('pingwin.jpg')

M= np.ones(image.shape, dtype="uint8") + 150
print(M)
added = cv2.add(image, M)

cv2.imshow('Original Image', image)
cv2.imshow('Added Image', added)

addedNP = image + M

cv2.imshow('Added Image with Numpy', addedNP)
print("Numpy ma duzo miejsc czarnych poniewaz zdjecie juz jest jasne wiec zaczyna od 0 ")

cv2.waitKey(0)