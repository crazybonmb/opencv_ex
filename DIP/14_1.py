import cv2
import numpy as np
img = cv2.imread('../image/test.jpg')
# 方法一 设置缩放比例
dst1 = cv2.resize(img, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC)

# 方法二 直接设置输出尺寸
height, width = img.shape[:2]  # 获得原尺寸
dst2 = cv2.resize(img, (int(2*width), int(2*height)), interpolation=cv2.INTER_CUBIC)  # 输出尺寸必须为整型
while(1):
    cv2.imshow('dst1', dst1)
    cv2.imshow('dst2', dst2)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
