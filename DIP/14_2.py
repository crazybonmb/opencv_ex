import cv2
import numpy as np

img = cv2.imread('test.jpg', 0)  # 以单通道灰度图像读入
rows, cols = img.shape
# 平移矩阵M：[[1,0,x],[0,1,y]]
M = np.float32([[1, 0, 200], [0, 1, 100]])
dst = cv2.warpAffine(img, M, (cols, rows))

while(1):
    cv2.imshow('dst', dst)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
