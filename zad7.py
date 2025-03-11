import cv2

image = cv2.imread('grafika.jpg')


(h, w) = image.shape[:2]


xstart = w//3
ystart = h//3
xend = w-w//3
yecd = h-h//3

image2=image[ystart:yecd, xstart:xend]

cv2.imshow('image1', image)
cv2.imshow('image2', image2)
cv2.waitKey(0)