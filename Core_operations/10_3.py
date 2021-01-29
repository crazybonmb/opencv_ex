import cv2
import numpy as np

img1 = cv2.imread('test5.jpg')
img2 = cv2.imread('logo.jpg')

rows, cols, channels = img2.shape  # 获取图像2的属性
roi = img1[125:125+rows, 125:125+cols]  # 选择roi范围

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # 转换为灰度图像
ret, mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)  # 非运算

img1_bg = cv2.bitwise_and(roi, roi, mask=mask)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)

dst = cv2.add(img1_bg, img2_fg)
img1[125:125+rows, 125:125+cols] = dst
cv2.imshow('result', img1)
cv2.imshow('mask', mask)
cv2.imshow('mask_imv', mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
