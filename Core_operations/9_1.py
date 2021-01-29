# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变默认输出的标准编码

img = cv2.imread('test.jpg')

# 获取像素值
px = img[100, 200]
print('图像(200,100)处的像素值为： ', px)

# 获取像素中的颜色值
blue = img[100, 200, 0]
print('图像(200,100)处的蓝色像素值为： ', blue)
print('图像(200,100)处的蓝色像素值为： ', img.item(100, 200, 0))

# 修改像素值
img[100, 200] = [0, 0, 0]
px = img[100, 200]
print('修改后图像(200,100)处的像素值为： ', px)
img.itemset((100, 200, 0), 128)
blue = img.item(100, 200, 0)
print('修改后图像(200,100)处的蓝色像素值为： ', blue)

cv2.imshow('modified', img)
k = cv2.waitKey(0)  # 始终检测键盘
if k == 27:  # 按ESC退出
    cv2.destroyAllWindows()
