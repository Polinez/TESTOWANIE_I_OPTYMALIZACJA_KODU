import argparse
import imutils
import cv2

image = cv2.imread("zdj.jpg")
cv2.imshow("Original", image)

kat=int(input("Podaj kat obrotu: "))

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY),kat, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)