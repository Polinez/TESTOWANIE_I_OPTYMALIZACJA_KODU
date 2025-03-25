import cv2

img = cv2.imread('zdj.jpg')
cv2.imshow('image', img)

print(img.shape)
resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow('resized', resized)
cv2.waitKey(0)
