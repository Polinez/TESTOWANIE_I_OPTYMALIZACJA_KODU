import cv2
import imutils

img = cv2.imread('zdj2.jpg')
cv2.imshow('image', img)
print(img.shape[0],img.shape[1])
resized = imutils.resize(img,width=800)
cv2.imshow('resized', resized)
cv2.imwrite("resized_output.jpg", resized)
cv2.waitKey(0)
