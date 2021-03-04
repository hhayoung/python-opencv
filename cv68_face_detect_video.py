## 비디오에서 정면 얼굴 검출 & 눈 검출 

import sys
import numpy as np
import cv2

cap = cv2.VideoCapture('./video/face_video.mp4')
# cap = cv2.VideoCapture('./video/cat_video.mp4') # 고양이는 검출 안 됨. 사람만 학습한 데이터라서
if not cap.isOpened():
    print('Video open failed')
    sys.exit()

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)


# Haar-like XML 파일 열기
classifier = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt2.xml')
classifier2 = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')
if classifier.empty() or classifier2.empty():
    print('XML load failed!')
    sys.exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = classifier.detectMultiScale(frame, scaleFactor=1.1, minSize=(24,24))
    # eyes = classifier2.detectMultiScale(frame, scaleFactor=1.1, minSize=(24,24))
    eyes = classifier2.detectMultiScale(frame, scaleFactor=1.2, minSize=(100,100)) # 조절했더니 눈 이외에 다른 것들 검출이 좀 줄었다.
    # minSize와 maxSize, 특히 minSize를 지정하면 속도가 좀 더 빨라진다. 지정안했을 때는 24x24 크기로 시작
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
    for (x, y, w, h) in eyes:
        cv2.circle(frame, (x+(w//2),y+(h//2)), w//2, (0,0,255), 2) 
        # 무식한 방법
        # 전체영역에서 중심찾는 거라서 이게 아니라 얼굴영역을 찾아놨으니까 각 얼굴영역에서 눈 위치를 찾아야 한다. 
    
    cv2.imshow('frame', frame)
    key = cv2.waitKey(delay)
    # 겁나 느림 -> 계산하는데 오래 걸려서 그런 것 같음. 
    # scaleFactor, minSize를 조절해주면 속도가 더 빨라진다. 그대신 검출은 더 안 됨.
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()