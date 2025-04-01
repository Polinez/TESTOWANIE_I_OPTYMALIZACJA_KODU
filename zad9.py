
import cv2

img = cv2.imread('img.jpg')

print(img.shape)

startX = img.shape[1]//2-50
endX = img.shape[1]//2+200

startY = img.shape[0]//2-200
endY = img.shape[0]//2+50

zegarek = img[startY:endY, startX:endX]

cv2.imwrite("cropped_image.jpg",zegarek)
print("img saved")

