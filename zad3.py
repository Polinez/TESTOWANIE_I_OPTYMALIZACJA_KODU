import cv2



image = cv2.imread('grafika.jpg')

(h, w) = image.shape[:2]

(b, g, r) = image[h//2, w//2]
print(f"Pixel at (x:{w//2} y:{h//2}) - Red:{r}, Green:{g}, Blue:{b}")