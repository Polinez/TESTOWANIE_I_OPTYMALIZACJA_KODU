import cv2

img = cv2.imread('img.jpg')

print(img.shape)

prawo = img[:, img.shape[1]//2:]
lewo = img[:, :img.shape[1]//2]

cv2.imshow("prawo",prawo)
cv2.imshow("zdjecie",img)
cv2.waitKey()