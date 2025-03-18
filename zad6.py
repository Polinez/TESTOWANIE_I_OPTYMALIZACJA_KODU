import numpy as np
import cv2

image = cv2.imread("osoba.jpg")
print(image.shape)
cv2.circle(image, (375,170), 25, (0, 0, 255), -1)
cv2.circle(image, (460,170), 25, (0, 0, 255), -1)

cv2.rectangle(image, (375, 300), (460, 250), (0, 255, 0), -1)
cv2.circle(image, (420, 175), 150, (255, 0, 0))
cv2.imshow("Image", image)
cv2.waitKey(0)