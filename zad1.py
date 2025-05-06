import cv2

image = cv2.imread("pies.jpg")
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (9, 9), (15, 15)]

for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow("Average ({}, {})".format(kX, kY), blurred) # ta metoda bardzo rozmywa obraz lecz dalej mozemy rozpoznac co znajduje sie na obrazie
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for (kX, kY) in kernelSizes:
    gauss = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow("Gaussian ({}, {})".format(kX, kY), gauss) # metoda gaussa troche gorzej rozmywa obraz lecz go nie nieksztalca
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for (kX, kY) in kernelSizes:
    median = cv2.medianBlur(image, kX)
    cv2.imshow("Median ({})".format(kX), median) ## ta metoda najbardziej znieksztalca obraz
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for (kX, kY) in kernelSizes:
    bilateral = cv2.bilateralFilter(image, kX, 75, 75) # ta funkcja praktycznie w ogole nie znieksztalca obrazu ale tez go nie rozmazuje
    cv2.imshow("Bilateral ({})".format(kX), bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()