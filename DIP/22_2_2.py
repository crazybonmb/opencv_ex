import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test22_1.jpg', 0)
# flatten() 将数组变成一维
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
# 计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

plt.subplot(321), plt.imshow(img, 'gray'), plt.axis('off')
plt.title('Original')

plt.subplot(322), plt.plot(cdf_normalized, color='b'),
plt.hist(img.flatten(), 256, [0, 256], color='r'),
plt.xlim([0, 256]),
plt.legend(('cdf', 'histogram'), loc='upper left'),
plt.title('Histogram')

img2 = cv2.equalizeHist(img)
hist2, bins = np.histogram(img2.flatten(), 256, [0, 256])
cdf2 = hist2.cumsum()
cdf_m = cdf2 * hist2.max() / cdf2.max()

plt.subplot(323), plt.imshow(img2, 'gray'), plt.axis('off')
plt.title('Histogram Equalization')

plt.subplot(324), plt.plot(cdf_m, color='b'),
plt.hist(img2.flatten(), 256, [0, 256], color='r'),
plt.xlim([0, 256]),
plt.legend(('cdf', 'histogram'), loc='upper left'),
plt.title('Histogram')

# 有限对比适应性直方图均衡化CLAHE（Contrast Limited Adaptive Histogram Equalization）
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
img3 = clahe.apply(img)
hist3, bins = np.histogram(img3.flatten(), 256, [0, 256])
cdf3 = hist3.cumsum()
cdf_m = cdf3 * hist3.max() / cdf3.max()

plt.subplot(325), plt.imshow(img3, 'gray'), plt.axis('off')
plt.title('CLAHE')

plt.subplot(326), plt.plot(cdf_m, color='b'),
plt.hist(img3.flatten(), 256, [0, 256], color='r'),
plt.xlim([0, 256]),
plt.legend(('cdf', 'histogram'), loc='upper left'),
plt.title('Histogram')

plt.show()
