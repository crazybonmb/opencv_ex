import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255, 0, 0]

img = cv2.imread('test.jpg')
replicate = cv2.copyMakeBorder(img, 30, 30, 30, 30, cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img, 30, 30, 30, 30, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img, 30, 30, 30, 30, cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img, 30, 30, 30, 30, cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img, 30, 30, 30, 30, cv2.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(cv2.cvtColor(replicate, cv2.COLOR_BGR2RGB), 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(cv2.cvtColor(reflect, cv2.COLOR_BGR2RGB), 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(cv2.cvtColor(reflect101, cv2.COLOR_BGR2RGB), 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(cv2.cvtColor(wrap, cv2.COLOR_BGR2RGB), 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(cv2.cvtColor(constant, cv2.COLOR_BGR2RGB), 'gray'), plt.title('CONSTANT')
plt.show()

'''
cv2.imshow('img', img)
cv2.imshow('replicate', replicate)
cv2.imshow('reflect', reflect)
cv2.imshow('reflect101', reflect101)
cv2.imshow('wrap', wrap)
cv2.imshow('constant', constant)

k = cv2.waitKey(0)  # 始终检测键盘
if k == 27:  # 按ESC退出
    cv2.destroyAllWindows()
'''
