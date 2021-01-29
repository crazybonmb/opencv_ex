import cv2
import numpy as np

img = cv2.imread('logo.jpg', 0)
img1 = cv2.countNonZero(img)
