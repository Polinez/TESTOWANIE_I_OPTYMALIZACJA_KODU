import cv2


image = cv2.imread('grafika.jpg')

(h, w) = image.shape[:2]

(xmax,ymax)=(0,0)

(b,g,r)=image[0, 0]
sum = b+g+r

for x in range(0, w-1):
    for y in range(0, h-1):
        if image[y, x].sum() > sum:
            sum = image[y, x].sum()
            (xmax, ymax) = (x, y)

print("brightness",sum)
print("x",xmax, "y",ymax)