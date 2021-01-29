import cv2
import numpy as np


def mouseEvent(event, x, y, flags, param):

    global img, position1, position2

    image = img.copy()

    if event == cv2.EVENT_LBUTTONDOWN:  # 按下左键
        position1 = (x, y)  # 获取鼠标的坐标(起始位置)

    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:  # 按住左键拖曳不放开
        cv2.rectangle(image, position1, (x, y), (0, 255, 0), 3)  # 画出矩形选定框
        cv2.imshow('image', image)

    elif event == cv2.EVENT_LBUTTONUP:  # 放开左键
        position2 = (x, y)  # 获取鼠标的最终位置
        cv2.rectangle(image, position1, position2, (0, 0, 255), 3)  # 画出最终的矩形
        cv2.imshow('image', image)

        min_x = min(position1[0], position2[0])  # 获得最小的坐标，因为可以由下往上拖动选定框
        min_y = min(position1[1], position2[1])
        width = abs(position1[0] - position2[0])  # 为了适配rect的格式
        height = abs(position1[1] - position2[1])

        mask = np.zeros(img.shape[:2], np.uint8)  # 初始化蒙版图像
        bgdModel = np.zeros((1, 65), np.float64)  # 内算法使用的零数组
        fgdModel = np.zeros((1, 65), np.float64)
        rect = (min_x, min_y, width, height)  # 选定的前景区域
        cv2.grabCut(image, mask, rect, bgdModel, fgdModel, 5,
                    cv2.GC_INIT_WITH_RECT)  # 函数返回值为mask,bgdModel,fgdModel
        mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype(
            'uint8')  # 代码中将0和2合并为背景 1和3合并为前景

        img1 = image*mask2[:, :, np.newaxis]  # 使用蒙板来获取前景区域
        cv2.imshow('GMM', img1)


def main():

    global img
    img = cv2.imread('test28.jpg', cv2.IMREAD_ANYCOLOR)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', mouseEvent)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
