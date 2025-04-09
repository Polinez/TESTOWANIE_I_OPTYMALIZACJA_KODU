import cv2
image = cv2.imread("rgb.jpg")
(B, G, R) = cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

print("Na kazdym kanale widzimy kolor ktory wystepuje na tym kanale")

cv2.waitKey(0)
cv2.destroyAllWindows()