import cv2
import numpy as np

img = cv2.imread('test1.jpg')
img = cv2.bilateralFilter(img, 13, 70, 50)  # 滤波降噪
box_roi = cv2.selectROI("roi", img)  # 选择roi区域
# 提取ROI图像
roi_img = img[box_roi[1]:box_roi[1]+box_roi[3],
             box_roi[0]:box_roi[0]+box_roi[2], :]
hsv1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(roi_img, cv2.COLOR_BGR2HSV)
hist1 = cv2.calcHist([hsv1], [0, 1], None, [180, 256], [0, 180, 0, 256])
hist2 = cv2.calcHist([hsv2], [0, 1], None, [180, 256], [0, 180, 0, 256])

# 使用Numpy中的算法
R = hist2/(hist1+1)  # 计算比值，加1 是为了避免除0
h, s, v = cv2.split(hsv1)
B = R[h.ravel(), s.ravel()]
B = np.minimum(B, 1)
B = B.reshape(hsv1.shape[:2])*255
# cv2.getStructuringElement用于构造一个特定形状的结构元素
# cv2.MORPH_ELLIPSE, (5, 5)表示构造一个5x5矩形内切椭圆用于卷积
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
B = cv2.filter2D(B, -1, disc)
B = np.uint8(B)
cv2.normalize(B, B, 0, 255, cv2.NORM_MINMAX)
ret, thresh = cv2.threshold(B, 50, 255, 0)
# 通道合并为3通道图像
thresh = cv2.merge((thresh, thresh, thresh))
# 使用形态学闭运算去除噪点
kernel = np.ones((5, 5), np.uint8)
mask = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
res = cv2.bitwise_and(img, mask)  # 与运算
cv2.imshow('Numpy', res)

# 利用 cv2.calcBackProject
# hist2是roi的直方图，将roi的直方图投影到原图的hsv空间得到mask
# 归一化之后的直方图便于显示，归一化之后就成了 0 到 255 之间的数了。
# 归一化并不必要
# cv2.normalize(hist2, hist2, 0, 255, cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsv1], [0, 1], hist2, [0, 180, 0, 256], 1)
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
cv2.filter2D(dst, -1, disc, dst)
out = cv2.merge([dst, dst, dst]) & img
cv2.imshow('OpenCV', out)
cv2.waitKey(0)
