import cv2
import numpy as np

img = cv2.imread('../image/test.jpg', 0)  # 以单通道灰度图像读入
rows, cols = img.shape
# 这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
# 可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.6)
# 第三个参数是输出图像的尺寸中心
dst = cv2.warpAffine(img, M, (cols, rows))
while(1):
    cv2.imshow('src', img)
    cv2.imshow('dst', dst)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
