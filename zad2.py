import numpy as np
import cv2

canvas = np.zeros((400,400, 3), dtype="uint8")

cv2.rectangle(canvas, (0,0), (100,15), (0, 255, 0))
cv2.rectangle(canvas, (canvas.shape[0]-100,canvas.shape[1]-15), (canvas.shape[0],canvas.shape[1]), (0, 0, 255), 3)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)