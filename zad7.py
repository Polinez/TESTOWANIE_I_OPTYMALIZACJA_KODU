import cv2
import imutils

img = cv2.imread('zdj.jpg')
cv2.imshow('image', img)
print(img.shape[0],img.shape[1])
resized = cv2.resize(img, (img.shape[1] // 5, img.shape[0] // 5), interpolation=cv2.INTER_AREA)
resized_linear = cv2.resize(img, (img.shape[1] // 5, img.shape[0] // 5), interpolation=cv2.INTER_LINEAR)
cv2.imshow('resized_area', resized)
cv2.imshow('resized_linear', resized_linear)
# jakos zostala na wysokim poiomie  a w liniowej bardzo sie pogorszyla 
cv2.waitKey(0)
