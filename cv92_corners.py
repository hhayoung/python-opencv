import sys
import numpy as np
import cv2


src = cv2.imread('./images/bd.png', cv2.IMREAD_GRAYSCALE)
# src = cv2.imread('./images/woodblock.png', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed!')
    sys.exit()

# 시간체크
tm = cv2.TickMeter()

## GFTT
tm.start()

corners = cv2.goodFeaturesToTrack(src, 400, 0.01, 10)

tm.stop()
print('GFTT: {}ms.'.format(tm.getTimeMilli()))

dst1 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# gftt는 keypoints X
if corners is not None:
    for i in range(corners.shape[0]):
        pt = (int(corners[i, 0, 0]), int(corners[i, 0, 1])) # 개수만큼
        cv2.circle(dst1, pt, 5, (0, 0, 255), 2)


## FAST
tm.reset()
tm.start()

# fast = cv2.FastFeatureDetector_create(60) # 보통 30~60준다
fast = cv2.FastFeatureDetector_create(30) # 더 많이 검출

# 비최대억제 설정
# fast.setNonmaxSuppression(0) # -> 비최대억제를 False로 하겠다. 기본값이 True

keypoints = fast.detect(src)

tm.stop()
print('FAST: {}ms.'.format(tm.getTimeMilli()))

dst2 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for kp in keypoints: # opencv가 제공하는 keypoints에는 좌표값이 들어있다. 좌표값을 얻으려면 멤버 pt를 이용해야 함.
    # pt[0]이 x좌표값, pt[1]이 y좌표값
    pt = (int(kp.pt[0]), int(kp.pt[1]))
    cv2.circle(dst2, pt, 5, (0, 0, 255), 2)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()