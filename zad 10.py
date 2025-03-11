import cv2
from scipy.special import xlog1py

image = cv2.imread('grafika.jpg')

(h, w) = image.shape[:2]

(b,g,r)=image[50,50]
(b2,g2,r2)=image[200,200]

print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
print("Pixel at (200, 200) - Red: {}, Green: {}, Blue: {}".format(r2, g2, b2))
print("difference: ",r-r2,g-g2,b-b2)