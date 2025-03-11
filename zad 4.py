import cv2

image = cv2.imread('grafika.jpg')
(h, w) = image.shape[:2]

x = int(input("Podaj współrzędną x: "))
y = int(input("Podaj współrzędną y: "))

if x < w and y < h:
    image[y, x] = (0, 0, 0)
    print("pixel at (", x, ",", y, ") changed to black")
else:
    print("out of range")