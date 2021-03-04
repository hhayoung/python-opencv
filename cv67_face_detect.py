## 정면 얼굴 검출 & 눈 검출 

# https://github.com/opencv/opencv/tree/master/data/haarcascades

# cv2.CascadeClassifier.detectMultiScale(image, scaleFactor=None, minNeighbors=None, flags=None, minSize=None, maxSize=None)
# image: 입력 영상
# scaleFactor: 기본값 1.1(영상 축소 비율), 기본값은 사각형의 크기를 1.1배로 점점 키워가면서 검출 
#               1.2로 지정하면 1.2배씩 사각형 크기를 키워가며 검출
#               축소 비율이 커지면 더 빨리 진행된다. 그대신 세밀하게 검출은 안 됨. 속도를 빨리 해야 하면 이 값을 키워주면 된다. 
# minNeighbors: 최종 검출 영역으로 설정하기 위한 사각형의 개수 지정, 기본값 3
# flags: 사용하지 않음
# minSize, maxSize: 보통 24,24부터 시작,  minSize를 지정해서 속도를 빠르게 할 수 있다.

import sys
import numpy as np
import cv2

# src = cv2.imread('./images/son2.png')
# src = cv2.imread('./images/son3.png')
src = cv2.imread('./images/son4.png')
if src is None:
    print('Image load failed!')
    sys.exit()

# 객체 생성 및 학습 데이터 불러오기(정면 얼굴 검출 & 눈 검출)
classifier = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt2.xml')
classifier2 = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')
# 또는 
# classifier = cv2.CascadeClassifier()
# classifier.load('./haarcascade_frontalface_alt2.xml')

if classifier.empty():
    print('XML load failed!')
    sys.exit()
if classifier2.empty():
    print('XML load failed!')
    sys.exit()

tm = cv2.TickMeter()
tm.start()

# 기본값은 1.1
# faces = classifier.detectMultiScale(src, scaleFactor=1.1)
faces = classifier.detectMultiScale(src, scaleFactor=1.1, minSize=(60,60)) # 얼굴말고 더 조그만한거 없애려고 minSize 키움ㄴ
eyes = classifier2.detectMultiScale(src, scaleFactor=1.1, minSize=(24,24))
# 리턴값은 사각형 좌표 (x,y,w,h) 

print(faces)
print(eyes)

tm.stop()
print(tm.getTimeMilli()) # minSize나 scaleFactor 인자값으로 바꿔가면서 시간차이 테스트
# scaleFactor=1.1 -> 149.3187
# scaleFactor=1.2 -> 130.8307
# scaleFactor=1.3 -> 123.18900000000001
# scaleFactor=1.4 -> 100.66120000000001
# scaleFactor=1.1, minSize=(24,24) -> 134.1301
# scaleFactor=1.1, minSize=(30,30) -> 122.29769999999999

for (x, y, w, h) in faces:
    cv2.rectangle(src, (x, y), (x+w, y+h), (255, 255, 0), 2)
for (x, y, w, h) in eyes:
    cv2.circle(src, (x+(w//2),y+(h//2)), w//2, (0,0,255), 2)

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()