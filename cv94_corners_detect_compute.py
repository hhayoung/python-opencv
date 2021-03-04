import sys
import numpy as np
import cv2


# 영상 불러오기
src1 = cv2.imread('./images/graf1.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('./images/graf3.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

# 특징점 알고리즘 객체 생성 (KAZE, AKAZE, ORB 등)
# feature = cv2.KAZE_create()
# feature = cv2.AKAZE_create()
feature = cv2.ORB_create()

# 특징점 검출 및 기술자 계산
kp1 = feature.detect(src1)
_, desc1 = feature.compute(src1, kp1) # compute() : 기술자 계산

kp2, desc2 = feature.detectAndCompute(src2, None) # detectAndCompute() : 검출하고 계산까지 한번에
# 검출만 하는 알고리즘을 사용할 때는 detectAndCompute()를 사용하면 실행x

print('desc1.shape:', desc1.shape)
print('desc1.dtype:', desc1.dtype)
print('desc2.shape:', desc2.shape)
print('desc2.dtype:', desc2.dtype)
# KAZE : 64열, 이것의 데이터타입은 float형이다 -> 실수 기술자 사용하고 있다.
# AKAZE : 61열, uint8 -> 이진 기술자 -> 해밍 디스턴스 방법을 적용해야 함.
# ORB : 32열, uint8 -> 이진 기술자 -> 해밍 디스턴스 방법을 적용해야 함.

# 검출된 특징점 출력 영상 생성
dst1 = cv2.drawKeypoints(src1, kp1, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
dst2 = cv2.drawKeypoints(src2, kp2, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()