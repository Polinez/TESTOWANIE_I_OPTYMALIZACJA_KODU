import cv2

img = cv2.imread('slon.jpg')
cv2.imshow('image', img)

horyzontaly=cv2.flip(img, 0)
cv2.imshow('horyzontaly', horyzontaly)

verticaly=cv2.flip(img, 1)
cv2.imshow('verticaly', verticaly)

fliped=cv2.flip(img, -1)
cv2.imshow('fliped', fliped)

cv2.waitKey(0)
