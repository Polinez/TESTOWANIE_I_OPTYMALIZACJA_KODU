import cv2

image = cv2.imread("samoyed.jpg")


cv2.namedWindow("Samoyed",cv2.WINDOW_NORMAL)
cv2.imshow("Samoyed", image)


cv2.waitKey(0)

cv2.destroyAllWindows()