import cv2
import numpy as np


def nothing(x):
    pass


# 当鼠标按下时变为 True
drawing = False  # 如果 mode 为 true 绘制矩形。按下'm' 变成绘制曲线。
mode = True
ix, iy = -1, -1
# 创建回调函数


def onmouse(event, x, y, flags, param):
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    color = (b, g, r)

    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:  # 按下左键
        drawing = True  # 开始绘制
        ix, iy = x, y  # 赋予按下时的鼠标坐标
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:  # 当按下左键拖拽鼠标时
        if drawing is True:
            if mode is True:
                cv2.rectangle(img, (ix, iy), (x, y), color, -1)  # 当模式为True时画矩形
            else:
                cv2.circle(img, (x, y), 3, color, 1)  # 当模式为False时画线
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        if drawing is True:
            if mode is True:
                cv2.circle(img, (x, y), 50, color, 3)  # 双击左键画空心圆
    elif event == cv2.EVENT_LBUTTONUP:  # 当鼠标松开停止绘画
        drawing is False
        if mode is True:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 255, 255), 5)   # 松开鼠标后画一个蓝色矩形


img = np.zeros((600, 800, 3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

cv2.setMouseCallback('image', onmouse)
while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()
