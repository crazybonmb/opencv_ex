import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('test30.jpg', 0)
# 创建ORB，由于图比较简单，所以设置的关键点数较小，默认500
orb = cv2.ORB_create(nfeatures=200)
# 使用ORB检测特征点
kp = orb.detect(img, None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# 绘制特征点
img2 = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)
plt.imshow(img2, cmap='gray'), plt.title('ORB'), plt.axis('off')
plt.show()
