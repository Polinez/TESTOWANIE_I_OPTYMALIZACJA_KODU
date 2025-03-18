import cv2
import imutils

image = cv2.imread("zdj.jpg")
cv2.imshow("Original", image)

rotated = imutils.rotate(image, 75)
cv2.imwrite("rotated_output.jpg", rotated)