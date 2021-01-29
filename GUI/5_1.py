import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret = cap.set(3, 320)  # 设置帧宽
ret = cap.set(4, 240)  # 设置帧高

if cap.isOpened() is True:
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 转换为灰色通道
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print('cap is not opened!')
