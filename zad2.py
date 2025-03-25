import cv2

img = cv2.imread('zdj.jpg')
cv2.imshow('image', img)
print(img.shape[0],img.shape[1])
resized = cv2.resize(img, (int(img.shape[1]*2), int(img.shape[0]*2)), interpolation=cv2.INTER_LINEAR)
cv2.imshow('resized', resized)
cv2.waitKey(0)
