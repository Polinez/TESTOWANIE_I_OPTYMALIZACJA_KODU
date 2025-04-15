import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('cienkie.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

iterations = range(1, 5)

results = []
for i in  range(1, 5):
        dilated = cv2.dilate(gray, None, iterations=i)
        white_pixels = np.sum(dilated == 255)
        results.append(white_pixels)
        cv2.imshow("Dilated {} times".format(i), dilated)
        cv2.waitKey(0)

plt.figure(figsize=(10, 6))
plt.plot(iterations, results, marker='o')
plt.xlabel('Liczba iteracji ')
plt.ylabel('Liczba białych pikseli (grubość)')
plt.xticks(iterations)
plt.tight_layout()

plt.show()

# obraz poogrubia wartosci co sprawia ze z liter ktore maja przerwy pomiedzy staja sie pelne
