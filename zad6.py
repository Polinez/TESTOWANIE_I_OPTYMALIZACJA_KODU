import cv2
import numpy as np

image = cv2.imread('pies.jpg')
cv2.imshow('Original', image)

mask = np.zeros(image.shape[:2],dtype="uint8")
cv2.circle(mask, (260,200),200,255,-1)

masked = cv2.bitwise_and(image, image, mask=mask)
#cv2.imshow('Masked', masked)


blurred_bg = cv2.GaussianBlur(image, (15, 15), 0)
#cv2.imshow('Blurred Background', blurred_bg)

mask_inv = cv2.bitwise_not(mask)
blurred_bg_masked = cv2.bitwise_and(blurred_bg, blurred_bg, mask=mask_inv)
cv2.imshow('Blurred Background Masked', blurred_bg_masked)

final = cv2.add(masked, blurred_bg_masked)
cv2.imshow('Final Result', final)

cv2.waitKey(0)
