import cv2


image = cv2.imread('grafika.jpg')
(h, w) = image.shape[:2]

image2 = image[0:h, 0:w].copy()

for x in range(50,100):
    for y in range(50,100):
        image2[y, x] = (255, 255, 255)
cv2.imshow("image2", image2)
cv2.imshow("image", image)
cv2.waitKey(0)