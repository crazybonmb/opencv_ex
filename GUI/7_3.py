import cv2
import numpy as np
import time

drawing = False  # 当鼠标按下变为True
mode = True  # 按下‘m’变成False，true为绘制矩形，false为画笔
ix, iy = -1, -1  # 初始化鼠标位置


def onmouse(event, x, y, flags, param):  # 创建回调函数
    global ix, iy, drawing, mode
    if event == cv2.EVENT_LBUTTONDOWN:  # 按下左键
        drawing = True  # 开始绘制
        ix, iy = x, y  # 赋予按下时的鼠标坐标
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:  # 当按下左键拖拽鼠标时
        if drawing is True:
            if mode is True:
                pass
                # cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)  # 当模式为True时画矩形
                # cv2.rectangle(img, (1, 1), (599, 599), (0, 0, 0), -1)
            else:
                cv2.circle(img, (x, y), 3, (0, 0, 255), -1)  # 当模式为False时画圆
    elif event == cv2.EVENT_LBUTTONUP:  # 当鼠标松开停止绘画
        drawing is False
        if mode is True:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 5)  # 松开鼠标后画一个蓝色矩形


img = np.zeros((600, 600, 3), np.uint8)  # 创建空图像
cv2.namedWindow('image')  # 创建空窗口
cv2.setMouseCallback('image', onmouse)  # 将回调函数与窗口绑定
while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):  # 按m更换模式
        mode = not mode
    elif k == 27:  # 按ESC退出
        break
cv2.destroyAllWindows()
