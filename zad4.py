import cv2

image = cv2.imread("znak.jpg")
cv2.imshow("Original", image)
kernelSizes = [(3, 3),(5, 5), (9, 9), (15, 15)]

for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
    # tekst jest nieczytelny na wielkosci 5x5 ale na wyzszych mozna sie domyslac co tam jest napisane
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for (kX, kY) in kernelSizes:
    gauss = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow("Gaussian ({}, {})".format(kX, kY), gauss)
# tutaj podobnie jak w poprzednim lecz mniej poniewaz na 15x15 rowniez da sie odczytac tekst ale najlepiej wyglada na 9x9
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for (kX, kY) in kernelSizes:
    median = cv2.medianBlur(image, kX)
    cv2.imshow("Median ({})".format(kX), median)
# tutaj rowniez tekst jest widoczny dla 5x5 ale na tych wyzszych totalnie nie da sie odczytac
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for (kX, kY) in kernelSizes:
    bilateral = cv2.bilateralFilter(image, kX, 75, 75)
    cv2.imshow("Bilateral ({})".format(kX), bilateral)
# ta metoda namniej rozmazuje tekst poniewaz nawet na wielkosci 15 dalej jest czytelny
cv2.waitKey(0)

cv2.destroyAllWindows()