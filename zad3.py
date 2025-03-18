import numpy as np
import cv2

image = cv2.imread("wiewiór.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]

tx = w // 2 + 50
ty = h // 2 + 50

M = np.float32([[1, 0, tx],
                [0, 1, ty]])

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Shifted Down and Right", shifted)

cv2.waitKey(0)
