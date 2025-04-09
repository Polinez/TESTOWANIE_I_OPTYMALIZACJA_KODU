import cv2
image = cv2.imread("rgb.jpg")
(B, G, R) = cv2.split(image)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

R50 = cv2.add(R, 150)
Rboost = cv2.merge([B, G, R50])
cv2.imshow("boosted", Rboost)

cv2.waitKey(0)
cv2.destroyAllWindows()