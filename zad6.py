import argparse
import imutils
import cv2

image = cv2.imread("zdj.jpg")
cv2.imshow("Original", image)


rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)