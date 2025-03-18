import cv2
import imutils

image = cv2.imread("zdj.jpg")

for i in range(0, 360, 15):
    rotated = imutils.rotate(image, i)
    cv2.imshow(f"Rotated by {i} Degrees", rotated)
    cv2.waitKey(500)