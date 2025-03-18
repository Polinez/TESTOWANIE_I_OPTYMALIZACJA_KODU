import cv2
import imutils
from joblib.testing import xfail

image = cv2.imread("wiewiór.jpg")

cv2.imshow("Original", image)

x=int(input("Podaj wartość przesunięcia w osi x: "))
y=int(input("Podaj wartość przesunięcia w osi y: "))

shifted = imutils.translate(image, x, y)
cv2.imshow("image", shifted)

cv2.waitKey(0)
