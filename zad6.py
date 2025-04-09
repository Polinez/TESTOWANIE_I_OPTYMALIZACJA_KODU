import cv2
import numpy as np
image = cv2.imread("cv2.png")
(B, G, R) = cv2.split(image)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

merged2 = cv2.merge([R, G, B])
cv2.imshow("switched", merged2)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 70, 50])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)

result = image.copy()
result[red_mask > 0] = [255, 255, 255]

cv2.imshow("deleted red", result)

cv2.waitKey(0)
cv2.destroyAllWindows()