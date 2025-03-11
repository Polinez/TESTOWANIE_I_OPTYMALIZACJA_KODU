import cv2
image = cv2.imread('grafika.jpg')
(h, w) = image.shape[:2]
print("y:",h, "x:",w)
cv2.imshow("Original", image)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

image[h-1,w-1] = (0,0,255)

(b, g, r) = image[h-1, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))


cv2.imshow("Modyfied", image)
cv2.waitKey(0)
