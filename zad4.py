import cv2

img = cv2.imread('img.jpg')

print("X=",img.shape[1])
print("Y=",img.shape[0])

startX=int(input("Podaj startX: "))
endX=int(input("Podaj endX: "))
startY=int(input("Podaj startY: "))
endY=int(input("Podaj endY: "))

wycinek = img[startY:endY, startX:endX]

cv2.imshow("wycinek",wycinek)
cv2.imshow("zdjecie",img)
cv2.waitKey()