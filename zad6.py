
import cv2

img = cv2.imread('img.jpg')

print(img.shape)

startX = img.shape[1]//2-50
endX = img.shape[1]//2+50

startY = img.shape[0]//2-50
endY = img.shape[0]//2+50

zegarek = img[startY:endY, startX:endX]

img[startY:endY, startX+250:endX+250] = zegarek


cv2.imshow("zdjecie",img)
cv2.waitKey()