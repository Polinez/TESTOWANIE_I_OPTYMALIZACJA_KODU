import cv2
import imutils

image = cv2.imread("wiewiór.jpg")

cv2.imshow("Original", image)

shifted = imutils.translate(image, 100, 50)
cv2.imshow("image", shifted)

cv2.waitKey(0)
