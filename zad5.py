import cv2
import numpy as np
image = cv2.imread('pingwin.jpg')
image2 = cv2.imread('pingwin.jpg')

startX = image.shape[1]//2-200
endX = image.shape[1]//2+300

startY = image.shape[0]//2-200
endY = image.shape[0]//2+200

pingwin = image[startY:endY, startX:endX]

image[startY+200:endY+200, startX:endX] = pingwin



cv2.imshow('original Image', image2)
cv2.imshow('moved', image)

cv2.imshow("diff",cv2.absdiff(image, image2))
print("diff odejmuje wartosci pikseli od siebie i jesli sa takie same to bedzie 0 czyli czarne a jak bedzie biale - mniej biale to bedzie troche jasniejsze niz czarne")

cv2.waitKey(0)


