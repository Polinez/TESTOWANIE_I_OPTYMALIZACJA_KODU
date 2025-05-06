import cv2
import numpy as np

image = cv2.imread("pies.jpg")
cv2.imshow("Original", image)

noise = np.zeros_like(image, dtype=np.float32)

cv2.randn(noise, 0, 25)

noisy_image = cv2.add(image, noise.astype(np.uint8))
cv2.imshow("Noisy", noisy_image)

kernelSizes = [(9,9)]

for (kX, kY) in kernelSizes:
    blurred = cv2.blur(noisy_image, (kX, kY))
    cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", noisy_image)

for (kX, kY) in kernelSizes:
    gauss = cv2.GaussianBlur(noisy_image, (kX, kY), 0)
    cv2.imshow("Gaussian ({}, {})".format(kX, kY), gauss)
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", noisy_image)

for (kX, kY) in kernelSizes:
    median = cv2.medianBlur(noisy_image, kX)
    cv2.imshow("Median ({})".format(kX), median)
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.imshow("Original", noisy_image)

for (kX, kY) in kernelSizes:
    bilateral = cv2.bilateralFilter(noisy_image, kX, 40, 40)
    cv2.imshow("Bilateral ({})".format(kX), bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()

# average tylko rozmazuje a nie uzuwa szumu
# tak samo w przypadku gaussa
# median sprawia ze szum znajduje sie w innym miejscu w takich jakby grupkach
# bilateralFiler nie zmienil szumu
