# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变默认输出的标准编码

img = cv2.imread('test.jpg')

# 获取图像属性
shape = img.shape
print('图像的形状为： ', shape)  # 打印图像形状，包括行、列、通道
size = img.size
print('图像的像素数目为： ', size)  # 打印图像的像素数目
dtype = img.dtype
print('图像的数据类型为： ', dtype)  # 打印图像的数据类型
