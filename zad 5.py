import cv2
image = cv2.imread('grafika.jpg')
(h, w) = image.shape[:2]

xMiddle = w // 2
yMiddle = h // 2

for i in range(0, xMiddle):
    for j in range(0, yMiddle):
        image[j, i] = (255, 0, 0)

cv2.imshow("Modyfied", image)
cv2.waitKey(0)