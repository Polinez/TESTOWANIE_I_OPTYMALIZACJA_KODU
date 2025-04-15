import cv2
import numpy as np

image = cv2.imread('cienkie.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", image)
kernelSizes = [(3, 3), (5, 5), (7, 7)]

for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(
    kernelSize[0], kernelSize[1]), closing)
    cv2.waitKey(0)

# znaki łacza sie przez co powstaja jakby byly bez przerw