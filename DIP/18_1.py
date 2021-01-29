import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test18.jpg', 0)

laplacian = cv2.Laplacian(img, -1)

sobel = cv2.Sobel(img, cv2.CV_8U, 1, 1, ksize=5)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
sobelx1 = cv2.Sobel(img, -1, 1, 0, ksize=-1)  # ksize=-1同样可以实现scharr
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=5)

scharr = cv2.Scharr(img, cv2.CV_8U, 0, 1)
scharrx = cv2.Scharr(img, cv2.CV_8U, 1, 0)
scharry = cv2.Scharr(img, cv2.CV_8U, 0, 1)

plt.subplot(241), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(242), plt.imshow(laplacian, cmap='gray'), plt.title('Laplacian')
plt.subplot(243), plt.imshow(sobel, cmap='gray'), plt.title('Sobel')
plt.subplot(244), plt.imshow(sobelx, cmap='gray'), plt.title('Sobel X')
plt.subplot(245), plt.imshow(sobelx1, cmap='gray'), plt.title('Scharr X')
plt.subplot(246), plt.imshow(scharrx, cmap='gray'), plt.title('Scharr X')
plt.subplot(247), plt.imshow(sobely, cmap='gray'), plt.title('Sobel Y')
plt.subplot(248), plt.imshow(scharry, cmap='gray'), plt.title('Scharr Y')

plt.show()
