import cv2

image = cv2.imread('grafika.jpg')
(h, w) = image.shape[:2]

xMiddle = w // 2
yMiddle = h // 2

for i in range(xMiddle-50, xMiddle+50):
    for j in range(yMiddle-50, yMiddle+50):
        image[j, i] = (0, 0, 255)


cv2.imshow("Modyfied", image)
cv2.waitKey(0)