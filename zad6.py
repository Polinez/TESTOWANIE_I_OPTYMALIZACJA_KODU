import cv2


img = cv2.imread('tablica.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", img)
# zamiana kolorow na czarno biale
gray = cv2.bitwise_not(gray)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
closed = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel, iterations=1)
opening = cv2.morphologyEx(closed, cv2.MORPH_OPEN, kernel)
cv2.imshow("Opening", opening)
cv2.imshow("closed", closed)



cv2.waitKey(0)


