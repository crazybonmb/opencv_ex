import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test22.jpg', 0)
# flatten() 将数组变成一维
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
# 计算累积分布图
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

plt.subplot(221), plt.imshow(img, 'gray'), plt.title('Original')

plt.subplot(222), plt.plot(cdf_normalized, color='b'),
plt.hist(img.flatten(), 256, [0, 256], color='r'),
plt.xlim([0, 256]),
plt.legend(('cdf', 'histogram'), loc='upper left'), plt.title('Histogram')

cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
# 对被掩盖的元素赋值，这里赋值为 0
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
img2 = cdf[img]
hist2, bins = np.histogram(img2.flatten(), 256, [0, 256])
cdf2 = hist2.cumsum()
cdf_m = cdf2 * hist2.max() / cdf2.max()

plt.subplot(223), plt.imshow(img2, 'gray'), plt.title('Equalized')

plt.subplot(224), plt.plot(cdf_m, color='b'),
plt.hist(img2.flatten(), 256, [0, 256], color='r'),
plt.xlim([0, 256]),
plt.legend(('cdf', 'histogram'), loc='upper left'), plt.title('Histogram')

plt.show()
