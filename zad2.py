import cv2
import numpy as np

image = cv2.imread("osoba-wysoko-wrazliwa-1024x576.jpg")
cv2.imshow("Original", image)

print(image.shape[0:2])
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (400, 110), (600, 130), 255, -1)
cv2.imshow("Rectangular Mask", mask)

masked = cv2.bitwise_and(image, image, mask=cv2.bitwise_not(mask))
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

