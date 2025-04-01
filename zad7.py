
import cv2

img = cv2.imread('img.jpg')

print(img.shape)

for i in range(3):
    for j in range(3):
        startX = j * img.shape[1]//3
        endX = (j + 1) * img.shape[1]//3
        startY = i * img.shape[0]//3
        endY = (i + 1) * img.shape[0]//3
        fragment = img[startY:endY, startX:endX]
        cv2.imshow(f"fragment{i},{j}", fragment)


cv2.waitKey()