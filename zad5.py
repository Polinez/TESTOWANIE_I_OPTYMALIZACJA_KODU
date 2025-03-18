import numpy as np
import cv2

canvas = np.zeros((300,300, 3), dtype="uint8")

for i in range(0, 300, 20):
    cv2.rectangle(canvas, (i, i), (300-i, 300-i), (0, 255, 0))

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)