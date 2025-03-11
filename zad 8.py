import cv2


image = cv2.imread('grafika.jpg')
(h, w) = image.shape[:2]

image2 = image[0:h, 0:w].copy()

for x in range(0, w):
    image2[100, x] = (0, 255, 0)
cv2.imshow("image2", image2)
cv2.imshow("image", image)
cv2.waitKey(0)