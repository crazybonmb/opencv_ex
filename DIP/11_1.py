import cv2
import numpy as np
import time

# 使用cv2.getTickCount()计时
img1 = cv2.imread('logo.jpg')
t1 = cv2.getTickCount()
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1, i)
t2 = cv2.getTickCount()
t = (t2 - t1)/cv2.getTickFrequency()
print('Result I got is ', t, ' seconds')

# 使用time.clock()计时
img2 = cv2.imread('logo.jpg')
start = time.clock()
for i in range(5, 49, 2):
    img2 = cv2.medianBlur(img2, i)
elapsed = (time.clock() - start)
print('Result I got is ', elapsed, ' seconds')
