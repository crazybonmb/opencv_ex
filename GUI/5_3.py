import numpy as np
import cv2

cap = cv2.VideoCapture('output.avi')  # 选择要播放的视频

if cap.isOpened() is True:
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 输出灰色图像
        cv2.imshow('frame', gray)
        if cv2.waitKey(25) & 0xFF == ord('q'):  # 改变cv2.waitKey()中的值可以改变播放速度
            break
    cap.release()
    cv2.destroyAllWindows()
else:
    print('cap is not opened!')
