import cv2

image = cv2.imread("samoyed.jpg")
image_black = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


cv2.imwrite("samoyed_black.jpg", image_black)