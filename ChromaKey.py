import cv2
import sys
import numpy as np


cap1 = cv2.VideoCapture('woman.mp4')
cap2 = cv2.VideoCapture('123.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('비디오를 열 수 없습니다')
    sys.exit()

cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 640, 360)

w=round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h=round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
frames_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frames_cnt2 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
print('frames_cnt1:',frames_cnt1)
print('frames_cnt2:',frames_cnt2)
fps = round(cap1.get(cv2.CAP_PROP_FPS))
print(fps)
delay = int(1000 / fps)

while True:
        ret1,frame1=cap1.read()
        ret2,frame2=cap2.read()

        if not ret2:
            break
        frame2 = cv2.resize(frame2, (w, h))

        # HSV 색 공간에서 녹색 영역을 검출하여 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255))  # 영상, 최솟값, 최댓값
        cv2.copyTo(frame2, mask, frame1)

        cv2.imshow('frame', frame1)
        key = cv2.waitKey(delay)

        if key==27:
                break

cap1.release()
cap2.release()
cv2.destroyAllWindows()