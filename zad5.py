
import cv2

img = cv2.imread('zdjOsoba.jpg')

print(img.shape)

startX = img.shape[1]//2-100
endX = img.shape[1]//2+100

startY = img.shape[0]//2-200
endY = img.shape[0]//2+150

twarz = img[startY:endY, startX:endX]


cv2.imshow("wycinek",twarz)
cv2.imshow("zdjecie",img)
cv2.waitKey()