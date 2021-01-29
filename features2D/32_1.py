import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test30.jpg')
img1 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)

cv2.drawKeypoints(gray, kp, img)
cv2.drawKeypoints(gray, kp, img1, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

plt.subplot(121), plt.imshow(img),
plt.title('Dstination'), plt.axis('off')
plt.subplot(122), plt.imshow(img1),
plt.title('Dstination'), plt.axis('off')
plt.show()
