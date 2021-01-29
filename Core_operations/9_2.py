import cv2
import numpy as np

img = cv2.imread('test.jpg')

cv2.imshow('original', img)

# 选择图像的一部分并复制到图像其他地方
part = img[1:215, 131:364]
img[216:430, 1:234] = part

cv2.imshow('modified', img)
k = cv2.waitKey(0)  # 始终检测键盘
if k == 27:  # 按ESC退出
    cv2.destroyAllWindows()
