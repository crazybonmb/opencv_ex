import cv2
import numpy as np


def nothing(x):  # 滑动条的回调函数
    pass


# 当鼠标按下时变为 True
drawing = False  # 如果 mode 为 true 绘制矩形。按下'm' 变成绘制曲线。
mode = True
ix, iy = -1, -1
# 创建回调函数


def onmouse(event, x, y, flags, param):  # 鼠标事件的回调函数
    r = cv2.getTrackbarPos('R', WindowName)  # 获取滑动条R值
    g = cv2.getTrackbarPos('G', WindowName)  # 获取滑动条G值
    b = cv2.getTrackbarPos('B', WindowName)  # 获取滑动条B值
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
                cv2.circle(img, (x, y), 3, color, -1)  # 当模式为False时画线
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        if drawing is True:
            if mode is True:
                cv2.circle(img, (x, y), 50, color, 3)  # 双击左键画空心圆
    elif event == cv2.EVENT_LBUTTONUP:  # 当鼠标松开停止绘画
        drawing is False
        if mode is True:
            cv2.rectangle(img, (ix, iy), (x, y), (255, 255, 255), 5)   # 松开鼠标后画一个白色矩形


top = cv2.imread('test3.jpg')  # 图片1
bottom = cv2.imread('test2.jpg')  # 图片2
img = np.zeros(top.shape, np.uint8)  # 以图片1的尺寸建立空的绘图图层
WindowName = 'example'  # 窗口名
cv2.namedWindow(WindowName, cv2.WINDOW_AUTOSIZE)  # 建立空窗口

cv2.createTrackbar('a1', WindowName, 0, 100, nothing)  # 两张图片间转换
cv2.createTrackbar('a2', WindowName, 0, 100, nothing)  # 图片与绘图间转换
cv2.createTrackbar('R', WindowName, 0, 255, nothing)  # 绘图颜色R
cv2.createTrackbar('G', WindowName, 0, 255, nothing)  # 绘图颜色G
cv2.createTrackbar('B', WindowName, 0, 255, nothing)  # 绘图颜色B

cv2.setMouseCallback(WindowName, onmouse)
while(1):
    a1 = cv2.getTrackbarPos('a1', WindowName)  # 获取a1滑动条值
    a2 = cv2.getTrackbarPos('a2', WindowName)  # 获取a2滑动条值
    overlap = cv2.addWeighted(bottom, 1-a1/100, top, a1/100, 0)  # 将两张图片相加
    adds = cv2.addWeighted(overlap, 1-a2/100, img, a2/100, 0)
    cv2.imshow(WindowName, adds)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv2.destroyAllWindows()
