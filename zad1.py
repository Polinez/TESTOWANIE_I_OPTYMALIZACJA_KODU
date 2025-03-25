import cv2

img = cv2.imread('slon.jpg')
cv2.imshow('image', img)

fliped=cv2.flip(img, 1)
cv2.imshow('fliped', fliped)

cv2.waitKey(0)
