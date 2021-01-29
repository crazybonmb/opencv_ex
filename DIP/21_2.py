import cv2
import numpy as np
from matplotlib import pyplot as plt

src = cv2.imread('test21_2.jpg')
img = src.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
length = cv2.arcLength(cnt, True)

epsilon = 0.08*length
approx = cv2.approxPolyDP(cnt, epsilon, True)
M = cv2.moments(approx)
area = cv2.contourArea(approx)
length1 = cv2.arcLength(approx, True)

cv2.drawContours(img, approx, -1, (0, 255, 0), 3)
cv2.polylines(img, [approx], True, (0, 255, 0), 3)

font = cv2.FONT_HERSHEY_SIMPLEX  # 设置字体样式
text = 'Area:  '+str(int(area))+'  Length:  '+str(int(length1))
cv2.putText(img, text, (10, 30), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)

plt.subplot(121), plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB)), plt.title('Src')
plt.subplot(122), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('image')
plt.show()
