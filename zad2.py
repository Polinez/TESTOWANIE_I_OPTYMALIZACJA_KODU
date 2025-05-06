import cv2

image = cv2.imread("pies.jpg")
cv2.imshow("Original", image)
kernelSizes = [(3, 3),(5, 5), (9, 9), (15, 15)]

for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow("Average ({}, {})".format(kX, kY), blurred) # najbardziej optymalnym jest obraz 9x9 aby nie utracic stotnych detali, wiekszy rozmiar juz stare sie nieczytelny
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for (kX, kY) in kernelSizes:
    gauss = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow("Gaussian ({}, {})".format(kX, kY), gauss) # tutaj rowniez najbardziej optymalna wielkoscia jest 9x9 aby nie utracic najwazniejszych elemrntow jak np wasy

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for (kX, kY) in kernelSizes:
    median = cv2.medianBlur(image, kX)
    cv2.imshow("Median ({})".format(kX), median) # tutaj rowniez 9 jest najbardziej optymalne a 15 juz za bardzo nieczytelne
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", image)

for (kX, kY) in kernelSizes:
    bilateral = cv2.bilateralFilter(image, kX, 75, 75) # tutaj natomiast nie widac duzych roznic i kazde ze zdjec jest bardzo podobne  i kazde jest czytelne
    cv2.imshow("Bilateral ({})".format(kX), bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()