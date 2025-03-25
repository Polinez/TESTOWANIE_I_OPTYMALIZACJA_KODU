import cv2

img = cv2.imread('zdj.jpg')
cv2.imshow('image', img)
print(img.shape[0],img.shape[1])
resized = cv2.resize(img, (300,200))
cv2.imshow('resized', resized)
cv2.waitKey(0)
