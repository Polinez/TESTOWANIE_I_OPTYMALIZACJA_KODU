import cv2


img = cv2.imread('update.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", img)

kernel_shapes = {
    'Kwadrat 5x5': cv2.MORPH_RECT,
    'Krzyż 5x5': cv2.MORPH_CROSS,
    'Elipsa 5x5': cv2.MORPH_ELLIPSE
}

operations = {
    'Erozja': cv2.MORPH_ERODE,
    'Dylatacja': cv2.MORPH_DILATE,
    'Otwarcie': cv2.MORPH_OPEN,
    'Zamknięcie': cv2.MORPH_CLOSE,
    'Gradient': cv2.MORPH_GRADIENT
}


for j, (op_name, op_type) in enumerate(operations.items(), 1):
    for i, (shape_name, shape_type) in enumerate(kernel_shapes.items(), 1):
        kernel = cv2.getStructuringElement(shape_type, (5, 5))
        result = cv2.morphologyEx(img, op_type, kernel)

        cv2.imshow(f"{shape_name} - {op_name}", result)
        cv2.waitKey(0 )



# shape type nie ma az takiego znaczenia do wyniku ale operacje morfologiczne sa duzo bardziej znaczace


cv2.waitKey(0)

