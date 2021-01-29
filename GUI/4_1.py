import cv2
import numpy as np
from matplotlib import pyplot as plt

for i in range(-1, 4):
    img = cv2.imread('test3.png', i)
    WindowName = 'image' + str(i)
    cv2.namedWindow(WindowName, cv2.WINDOW_AUTOSIZE)  # 建立空窗口
    cv2.imshow(WindowName, img)
    # cv2.resizeWindow(WindowName, 500, 312) # 定义窗口大小
    k = cv2.waitKey(0)  # 始终检测键盘
    if k == 27:  # 按ESC退出
        cv2.destroyAllWindows()
    elif k == ord('s'):  # 按s保存
        cv2.imwrite(WindowName+'.png', img)
        cv2.destroyAllWindows()
    elif k == ord('p'):  # 按p用matplotlib打开
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 将opencv用的的BGR通道顺序变为plt用的RGB顺序
        plt.imshow(rgb)
        plt.xticks([]), plt.yticks([])
        plt.show()
