import numpy as np
import cv2

canvas = np.zeros((300,300, 3), dtype="uint8")

cv2.circle(canvas, (0,0), 40, (255, 0, 0))
cv2.circle(canvas, (canvas.shape[0]//2,canvas.shape[1]//2), 60, (0, 0, 255))

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)