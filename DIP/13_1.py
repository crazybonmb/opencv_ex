import matplotlib.pyplot as plt
import cv2

img_BGR = cv2.imread('test.jpg')  # BGR
plt.subplot(331), plt.imshow(img_BGR), plt.axis('off'), plt.title('BGR')

img_RGB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)
plt.subplot(332), plt.imshow(img_RGB), plt.axis('off'), plt.title('RGB')

img_GRAY = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
plt.subplot(333), plt.imshow(img_GRAY), plt.axis('off'), plt.title('GRAY')

img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
plt.subplot(334), plt.imshow(img_HSV), plt.axis('off'), plt.title('HSV')

img_YcrCb = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YCrCb)
plt.subplot(335), plt.imshow(img_YcrCb), plt.axis('off'), plt.title('YcrCb')

img_HLS = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HLS)
plt.subplot(336), plt.imshow(img_HLS), plt.axis('off'), plt.title('HLS')

img_XYZ = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2XYZ)
plt.subplot(337), plt.imshow(img_XYZ), plt.axis('off'), plt.title('XYZ')

img_LAB = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2LAB)
plt.subplot(338), plt.imshow(img_LAB), plt.axis('off'), plt.title('LAB')

img_YUV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2YUV)
plt.subplot(339), plt.imshow(img_YUV), plt.axis('off'), plt.title('YUV')
plt.show()

cv2.imshow('gray', img_GRAY)

k = cv2.waitKey(0)  # 始终检测键盘
if k == 27:  # 按ESC退出
    cv2.destroyAllWindows()
