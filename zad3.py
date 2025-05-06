import cv2

image = cv2.imread("ostre.jpg")
cv2.imshow("Original", image)

params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]
for (diameter, sigmaColor, sigmaSpace) in params:
    blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
    title = "Blurred d={}, sc={}, ss={}".format(diameter, sigmaColor, sigmaSpace)
    cv2.imshow(title, blurred)

blurred = cv2.GaussianBlur(image, (9, 9), 0)
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)

# rozmycie 2 strone skutecznie usunelo szum w postaci takich czerwonych kropek w tle
# ta metoda rowniez pozostawila ostre krawedzie w porownaniu do kausowkiego ktora tylko obraz rozmyla redukujac tylko w niewielkim stopniu szum
# moim zdaniem najlepsze rezultaty daja parametry simga color 41 oraz 61 poniewaz najbardziej redukuje szum