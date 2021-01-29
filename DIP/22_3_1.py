import cv2
import numpy as np


# 定义回调函数
def set_scale(val):
    global hist_scale
    hist_scale = val


# 构建HSV颜色地图
hsv_map = np.zeros((180, 256, 3), np.uint8)
h, s = np.indices(hsv_map.shape[:2])
hsv_map[:, :, 0] = h
hsv_map[:, :, 1] = s
hsv_map[:, :, 2] = 255
hsv_map = cv2.cvtColor(hsv_map, cv2.COLOR_HSV2BGR)
cv2.imshow('hsv_map', hsv_map)

cv2.namedWindow('hist', 0)
hist_scale = 10

cv2.createTrackbar('scale', 'hist', hist_scale, 32, set_scale)

while(True):
    frame = cv2.imread('test1.jpg')
    cv2.imshow('camera', frame)
    # 通过图像金字塔降低分辨率，但不会对直方图有太大影响。
    # 但这种低分辨率，可以很好抑制噪声，从而去除孤立的小点对直方图的影响
    small = cv2.pyrDown(frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 取 v 通道 (亮度) 的值。
    dark = hsv[:, :, 2] < 32
    hsv[dark] = 0
    h = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    h = np.clip(h*0.005*hist_scale, 0, 1)
    vis = hsv_map*h[:, :, np.newaxis] / 255.0
    cv2.imshow('hist', vis)

    ch = 0xFF & cv2.waitKey(1)
    if ch == 27:
        break
cv2.destroyAllWindows()
