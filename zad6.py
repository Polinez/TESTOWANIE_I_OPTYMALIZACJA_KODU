import cv2
import imutils

img = cv2.imread('zdj.jpg')
cv2.imshow('image', img)
print(img.shape[0],img.shape[1])
resized = imutils.resize(img,height=400)
cv2.imshow('resized', resized)
cv2.waitKey(0)
