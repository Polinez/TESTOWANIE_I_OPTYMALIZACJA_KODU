import cv2


img = cv2.imread('zdj.jpg')
cv2.imshow('image', img)
print(img.shape[0],img.shape[1])
for i in range(100, 300, 20):
    new_width = int(img.shape[1] * (i/100))
    new_height = int(img.shape[0] * (i/100))
    resized = cv2.resize(img, (new_width, new_height))
    cv2.imshow(f'resized{i}', resized)
    cv2.waitKey(500)

