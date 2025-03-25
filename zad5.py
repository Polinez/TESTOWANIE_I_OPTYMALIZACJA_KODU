import cv2
from scipy.special import y1_zeros

img = cv2.imread('slon.jpg')
cv2.imshow('image', img)

print(img.shape[0], img.shape[1])

cropp_range=1000
y1,y2 = img.shape[0]//2-cropp_range, img.shape[0]//2+cropp_range
x1,x2 = img.shape[1]//2-cropp_range, img.shape[1]//2+cropp_range

middle = img[y1:y2, x1:x2]
flipped_middle = cv2.flip(middle, -1)

img[y1:y2, x1:x2] = flipped_middle

cv2.imshow('fliped_middle', img)

cv2.waitKey(0)
