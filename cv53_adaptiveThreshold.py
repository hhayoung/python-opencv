# adaptiveThreshold 함수를 이용한 지역 이진화
# cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst)
# src: 그레이스케일 영상(입력), maxValue: 최대값 255
# adaptiveMethod: 블럭 평균 계산 방법 지정, cv2.ADAPTIVE_THRESH_MEAN_C(평균)
#                                         cv2.ADAPTIVE_THRESH_GAUSSIAN_C(가중치 평균) - 블러처리하는 것
# thresholdType: BINARY, BINARY_INV 앞과 동일하게 둘 중에 하나 지정
# blockSize: 보통 홀수로 지정(3이상의 값)
# C: adaptiveMethod에서 지정한 블러링된 영상의 (x,y)좌표값에서 빼는 값. 뺀 값을 임계값으로 사용하겠다는 의미.
# 지역이진화를 위해 블러링을 하게 되는데(2가지 중 하나 선택) 블러링 한 영상의 (x,y)에서 C값을 빼주면 그게 임계값
# dst: 출력영상

import cv2, sys, numpy as np

# src = cv2.imread('./images/rice.png', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('./images/sudoku.jpg', cv2.IMREAD_GRAYSCALE)
if src is None:
    print("Image load failed")
    sys.exit()

def on_trackbar(pos):
    bsize = pos
    if bsize % 2 == 0:
        bsize = bsize - 1  # 홀수로 만듦
    if bsize < 3:
        bsize = 3

    dst = cv2.adaptiveThreshold(src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, bsize, 5) # C값 꼭 써줘야 함.

    cv2.imshow('dst', dst)

cv2.imshow('src', src)
cv2.namedWindow('dst')
cv2.createTrackbar('Block Size', 'dst', 0, 200, on_trackbar)
cv2.setTrackbarPos('Block Size', 'dst', 11)


cv2.waitKey()

cv2.destroyAllWindows()