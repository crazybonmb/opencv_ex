import numpy as np
import cv2

img = np.zeros((512, 512, 3), dtype=np.uint8)  # 设置窗口尺寸和数据类型
# cv2.line(img, (200, 100), (300, 200), (255, 0, 0), 1)
# cv2.line(img, (200, 200), (300, 300), (0, 255, 0), 5, 4)
# cv2.line(img, (200, 300), (300, 400), (0, 0, 255), 10, cv2.LINE_AA)
# cv2.rectangle(img, (350, 255), (511, 511), (0, 255, 0), 1)
# cv2.rectangle(img, (350, 255), (511, 511), (0, 0, 255), -1, shift=1)
# cv2.circle(img, (255, 255), 63, (0, 0, 255), -1)
# cv2.circle(img, (255, 255), 63, (255, 0, 0), 1, shift=1)
# cv2.ellipse(img, (160, 256), (100, 50), 0, 0, 240, (0, 255, 0), -1)
# cv2.ellipse(img, (400, 256), (100, 50), 60, 0, 240, (0, 255, 0), -1)
# a = np.array([[[10, 10], [100, 10], [100, 100], [10, 100]]], dtype=np.int32)
# b = np.array([[[150, 100], [250, 230], [200, 200], [150, 220]]], dtype=np.int32)
# c = np.array([[[300, 300], [400, 430], [350, 400], [300, 420]]], dtype=np.int32)
# cv2.fillPoly(img, a, (255, 0, 0))
# cv2.polylines(img, b, 0, (0, 255, 0))
# cv2.polylines(img, c, 1, (0, 255, 0))
# cv2.fillPoly(img, b, (255, 0, 0))
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 300), font, 4, (0, 255, 0), 2, cv2.LINE_AA, 0)
cv2.putText(img, 'OpenCV', (10, 300), font, 4, (255, 0, 0), 2, cv2.LINE_AA, 1)
WindowsName = 'example'
cv2.namedWindow(WindowsName)
cv2.imshow(WindowsName, img)
cv2.waitKey(0)
cv2.destroyWindow(WindowsName)
