import cv2
from sqlalchemy.util import methods_equivalent

img = cv2.imread('zdj2.jpg')
cv2.imshow('image', img)
print(img.shape[0],img.shape[1])
methods = [
("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
for (name,method) in methods:
    resized = cv2.resize(img, (img.shape[1]*3, img.shape[0]*3), interpolation=method)
    cv2.imshow(name, resized)
    cv2.waitKey(0)

cv2.waitKey(0)
