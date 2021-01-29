import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 设置视频编码格式
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # 名称， 格式， 帧率， 帧大小

if cap.isOpened() is True:  # 如果摄像头已被初始化返回True
    while(True):
        ret, frame = cap.read()  # 如果帧读取正确则返回True
        if ret is True:
            frame = cv2.flip(frame, 1)  # 反转图像，0：垂直反转，1：水平翻转，2：水平垂直反转
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cap.release()
    cv2.destroyAllWindows()
else:
    print('cap is not opened!')
