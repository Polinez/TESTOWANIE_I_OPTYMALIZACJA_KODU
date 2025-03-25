import cv2
import imutils

img = cv2.imread('zdj2.jpg')
cv2.imshow('image', img)
print(img.shape[0],img.shape[1])
INTER_CUBIC = cv2.resize(img, (img.shape[1] *4, img.shape[0] *4), interpolation=cv2.INTER_CUBIC)
INTER_LANCZOS4 = cv2.resize(img, (img.shape[1] *4, img.shape[0] *4), interpolation=cv2.INTER_LANCZOS4)
cv2.imshow('resized_area', INTER_CUBIC)
cv2.imshow('INTER_LANCZOS4', INTER_LANCZOS4)
# nie widac znaczacych roznic 
cv2.waitKey(0)
