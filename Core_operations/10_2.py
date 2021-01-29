import cv2
import numpy as np
from matplotlib import pyplot as plt


def nothing(x):  # 滑动条的回调函数
    pass


top = cv2.imread('test5.jpg')  # 图片1
bottom = cv2.imread('test6.jpg')  # 图片2
WindowName = 'example'  # 窗口名
cv2.namedWindow(WindowName, cv2.WINDOW_AUTOSIZE)  # 建立空窗口

cv2.createTrackbar('proportion', WindowName, 0, 100, nothing)  # 两张图片间转换

img1 = cv2.addWeighted(bottom, 0, top, 1, 0)
img2 = cv2.addWeighted(bottom, 0.3, top, 0.7, 0)
img3 = cv2.addWeighted(bottom, 0.5, top, 0.5, 0)
img4 = cv2.addWeighted(bottom, 0.7, top, 0.3, 0)
img5 = cv2.addWeighted(bottom, 1, top, 0, 0)


plt.subplot(231), plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB), 'gray'), plt.title('0:10')
plt.subplot(232), plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB), 'gray'), plt.title('3:7')
plt.subplot(233), plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB), 'gray'), plt.title('5:5')
plt.subplot(234), plt.imshow(cv2.cvtColor(img4, cv2.COLOR_BGR2RGB), 'gray'), plt.title('7:3')
plt.subplot(235), plt.imshow(cv2.cvtColor(img5, cv2.COLOR_BGR2RGB), 'gray'), plt.title('10:0')

while(1):
    a1 = cv2.getTrackbarPos('proportion', WindowName)  # 获取a1滑动条值
    overlap = cv2.addWeighted(bottom, 1-a1/100, top, a1/100, 0)  # 将两张图片相加
    cv2.imshow(WindowName, overlap)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('m'):  # 按m输出matplotlib绘图
        plt.show()
cv2.destroyAllWindows()
