import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()  # 读取视频帧
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # 转换为HSV空间

    # 注意是HSV参数，HSV空间中，H表示色调，取值范围 [0，179]，S表示饱和度，取值范围 [0，255]，V表示亮度，取值范围 [0，255]
    lower_blue = np.array([80, 50, 0])  # 设定蓝色的阈值
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)  # 设定取值范围
    res = cv2.bitwise_and(frame, frame, mask=mask)  # 对原图像处理

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
