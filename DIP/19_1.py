import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../image/test32.jpg', 0)
edges = cv2.Canny(img, 50, 100)
edges2 = cv2.Canny(img, 50, 150)
edges3 = cv2.Canny(img, 50, 200)
edges4 = cv2.Canny(img, 100, 150)
edges5 = cv2.Canny(img, 200, 250)

plt.subplot(231), plt.imshow(img, cmap='gray'), plt.title('Original Image')
plt.subplot(232), plt.imshow(edges, cmap='gray'), plt.title('Edge Image 50,100')
plt.subplot(233), plt.imshow(edges2, cmap='gray'), plt.title('Edge Image 50,100')
plt.subplot(234), plt.imshow(edges3, cmap='gray'), plt.title('Edge Image 50,100')
plt.subplot(235), plt.imshow(edges4, cmap='gray'), plt.title('Edge Image 50,100')
plt.subplot(236), plt.imshow(edges5, cmap='gray'), plt.title('Edge Image 50,100')

plt.show()
