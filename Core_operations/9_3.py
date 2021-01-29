import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg')
cv2.imshow('original', img)

# 分离颜色通道
b, g, r = cv2.split(img)
cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)

# 其他方法
b1 = img[:, :, 0]  # 仅取B通道
cv2.imshow('Blue-1', b1)
b2 = cv2.imread('test.jpg')
b2[:, :, 1:3] = 0  # 将0赋值给G、R通道
cv2.imshow('Blue-2', b2)

merge = cv2.merge([b, g, r])
cv2.imshow('merge', merge)

k = cv2.waitKey(0)  # 始终检测键盘
if k == 27:  # 按ESC退出
    cv2.destroyAllWindows()
