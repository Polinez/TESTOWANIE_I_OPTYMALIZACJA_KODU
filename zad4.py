import numpy as np
import cv2

canvas = np.zeros((300,300, 3), dtype="uint8")

cv2.rectangle(canvas, (canvas.shape[0]//2-50,canvas.shape[1]//2-50), (canvas.shape[0]//2+50,canvas.shape[1]//2+50), (255, 255, 255), -1)
cv2.circle(canvas, (canvas.shape[0]//2,canvas.shape[1]//2), 30, (0, 0, 255),-1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)