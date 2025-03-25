import cv2

img = cv2.imread('slon.jpg')
cv2.imshow('image', img)

flipped_direction = int(input('enter flip direction (0 - horizontal, 1 - vertical, -1 - both): '))

if flipped_direction not in [0, 1, -1]:
    print('Invalid input')
else:
    fliped=cv2.flip(img, flipped_direction)
    cv2.imshow('fliped', fliped)

    cv2.waitKey(0)
