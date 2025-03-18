import argparse
import imutils
import cv2

image = cv2.imread("zdj.jpg")
cv2.imshow("Original", image)



rotated = imutils.rotate(image, 30)
rotated = imutils.rotate(rotated, 30)
rotated = imutils.rotate(rotated, 30)
cv2.imshow("imutils", rotated)
cv2.waitKey(0)


rotated = imutils.rotate(image, 90)
cv2.imshow("imutils", rotated)
cv2.waitKey(0)
