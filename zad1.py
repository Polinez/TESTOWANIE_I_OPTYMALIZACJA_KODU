import numpy as np
import cv2

triangle = np.zeros((300, 300), dtype="uint8")
cv2.fillPoly(triangle, [np.array([[150, 50], [50, 250], [250, 250]])], 255)
cv2.imshow("Triangle", triangle)

circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

bitwiseAND = cv2.bitwise_and(triangle, circle)
cv2.imshow("Bitwise AND", bitwiseAND)
bitwiseOR = cv2.bitwise_or(triangle, circle)
cv2.imshow("Bitwise OR", bitwiseOR)
bitwiseXOR= cv2.bitwise_xor(triangle, circle)
cv2.imshow("Bitwise XOR", bitwiseXOR)
bitwiseNOT = cv2.bitwise_not(triangle)
cv2.imshow("Bitwise NOT", bitwiseNOT)

bitwiseXOR = cv2.bitwise_xor(circle, triangle)
cv2.imshow("Bitwise XOR v2", bitwiseXOR)

bitwiseOR = cv2.bitwise_or(circle, triangle)
cv2.imshow("Bitwise OR v2", bitwiseOR)
print("Pozycja nie ma znaczenia")

cv2.waitKey()