
import cv2

img = cv2.imread('img.jpg')
img2 = cv2.imread('img.jpg')

print(img.shape)

for i in range(0, img.shape[1], 10):
    startX = i
    endX = img.shape[1]
    img2[:, startX:endX] = img[:, startX:endX]
    cv2.imshow(f"fragment{i}", img2[:, startX:endX])
    cv2.waitKey(1)
    cv2.destroyAllWindows()




