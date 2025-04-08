
import cv2

img = cv2.imread('img.jpg')

print(img.shape)

startX = img.shape[1]//2-50
endX = img.shape[1]//2+50

startY = img.shape[0]//2-50
endY = img.shape[0]//2+50

zegarek = img[startY:endY, startX:endX]

img2 = img.copy()
img2[startY:endY, startX+250:endX+250] = zegarek


cv2.imshow("zdjecie",img)
cv2.imshow("zegarek", img2)


XOR =cv2.bitwise_xor(img, img2)

cv2.imshow("XOR", XOR)

cv2.waitKey()