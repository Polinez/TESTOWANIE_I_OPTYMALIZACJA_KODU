import cv2

img = cv2.imread('img.jpg')

print(img.shape)

dol = img[img.shape[0]//2:, :]
gora = img[0:img.shape[0]//2, :]

cv2.imshow("dol",dol)
cv2.imshow("zdjecie",img)
cv2.waitKey()