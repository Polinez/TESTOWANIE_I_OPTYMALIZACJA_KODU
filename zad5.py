import cv2
import numpy as np


image = cv2.imread("auto.jpg")
cv2.imshow("Original", image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

min_red1 = np.array([0, 70, 50])#RGB
max_red1 = np.array([10, 255, 255])
min_red2 = np.array([160, 70, 50])
max_red2 = np.array([180, 255, 255])

mask_red1 = cv2.inRange(hsv, min_red1, max_red1)
mask_red2 = cv2.inRange(hsv, min_red2,max_red2)
mask_red = cv2.bitwise_or(mask_red1, mask_red2)

final = cv2.bitwise_and(image, image, mask=mask_red)

cv2.imshow("Mask", mask_red)
cv2.imshow("Extracted", final)

(B, G, R) = cv2.split(final)

R_boosted = cv2.add(R, 100)
R_final = np.where(mask_red > 0, R_boosted, R)

merged = cv2.merge([B, G, R_final])
cv2.imshow("Merged", merged)
cv2.waitKey(0)