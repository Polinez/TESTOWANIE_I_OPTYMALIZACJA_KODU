import cv2

image = cv2.imread("samoyed.jpg")
image_black = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if len(image_black.shape) == 2:
    print("Liczba kanałów w obrazie w odcieniach szarości: 1")
else:
    print(f"Liczba kanałów: {image_black.shape[2]}")

cv2.imshow("Samoyed", image)

cv2.imshow("Samoyed black", image_black)

cv2.waitKey(0)
