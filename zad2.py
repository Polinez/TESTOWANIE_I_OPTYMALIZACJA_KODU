import cv2

image = cv2.imread("samoyed.jpg")

(h,w,c) = image.shape[:3]
print(f"Głębia kolorów: {c}")