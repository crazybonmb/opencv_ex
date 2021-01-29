import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test2.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.axis('off'),
plt.title('Original')

plt.subplot(122), plt.imshow(hist, interpolation='nearest'),
plt.title('2D Histogram')

plt.show()
