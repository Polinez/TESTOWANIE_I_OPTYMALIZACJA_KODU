import cv2
import numpy as np
image = cv2.imread("rgb.jpg")
(B, G, R) = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

merged = cv2.merge([R, G, B])
cv2.imshow("Merged", merged)

zeroR = cv2.merge([R, G, np.zeros_like(R)])
cv2.imshow("zeroR", zeroR)

print("Wyswietlenie w innej kolejnosci kanalow zmienia kolory np zólty na niebieski")
print("zmiana kanalu na zero powoduje usuniecie tego koloru")

cv2.waitKey(0)
cv2.destroyAllWindows()