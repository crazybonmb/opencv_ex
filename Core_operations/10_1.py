import cv2
import numpy as np
from matplotlib import pyplot as plt

x = np.uint8([250])
y = np.uint8([10])
print(cv2.add(x, y))
print(x+y)

img1 = cv2.imread('test5.jpg')  # 图片1
img2 = cv2.imread('test6.jpg')  # 图片2
add = cv2.add(img1, img2)  # 两个图像相加
subtract = cv2.subtract(img1, img2)  # 两个图像相减
multiply = cv2.multiply(img1, img2)  # 两个图像相乘
divide = cv2.divide(img1, img2)  # 两个图像相除

plt.subplot(231), plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB), 'gray'), plt.title('img1')
plt.subplot(232), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB), 'gray'), plt.title('img2')
plt.subplot(233), plt.imshow(cv2.cvtColor(add, cv2.COLOR_BGR2RGB), 'gray'), plt.title('add')
plt.subplot(234), plt.imshow(cv2.cvtColor(subtract, cv2.COLOR_BGR2RGB), 'gray'), plt.title('subtract')
plt.subplot(235), plt.imshow(cv2.cvtColor(multiply, cv2.COLOR_BGR2RGB), 'gray'), plt.title('multiply')
plt.subplot(236), plt.imshow(cv2.cvtColor(divide, cv2.COLOR_BGR2RGB), 'gray'), plt.title('divide')
plt.show()
