import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('test37_0.jpg', 0)  # queryImage
img2 = cv2.imread('test37_1.jpg', 0)

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# Apply ratio test # 比值测试，首先获取与 A 距离最近的点 B（最近）和 C（次近），
# 只有当 B/C # 小于阈值时（0.75）才被认为是匹配，因为假设匹配是一一对应的，真正的匹配的理想距离为 0
good = []
for m, n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good[:20], None, flags=2)
plt.imshow(img3, cmap='gray'), plt.title('Matched Result'), plt.axis('off')
plt.show()
