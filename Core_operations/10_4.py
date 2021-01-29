import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('test5.jpg')  # 图片1
img2 = cv2.imread('test6.jpg')  # 图片2
band = cv2.bitwise_and(img1, img2)  # 两个图像求交
bor = cv2.bitwise_or(img1, img2)  # 两个图像求并
bnot = cv2.bitwise_not(img1)  # 图像求非
bxor = cv2.bitwise_xor(img1, img2)  # 两个图像求异或

plt.subplot(231), plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB), 'gray'), plt.title('img1')
plt.subplot(232), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB), 'gray'), plt.title('img2')
plt.subplot(233), plt.imshow(cv2.cvtColor(band, cv2.COLOR_BGR2RGB), 'gray'), plt.title('and')
plt.subplot(234), plt.imshow(cv2.cvtColor(bor, cv2.COLOR_BGR2RGB), 'gray'), plt.title('or')
plt.subplot(235), plt.imshow(cv2.cvtColor(bnot, cv2.COLOR_BGR2RGB), 'gray'), plt.title('not')
plt.subplot(236), plt.imshow(cv2.cvtColor(bxor, cv2.COLOR_BGR2RGB), 'gray'), plt.title('xor')
plt.show()
