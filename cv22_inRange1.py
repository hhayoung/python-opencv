## 특정 컬러 영역 추출하기

# 특정 영역 안에 있는 컬러를 추출하는 함수
# cv2.inRange(src, lowerb, upperb, dst)
# lowerb: 하한 값, upperb: 상한 값 (스칼라값이나 행렬)

'''
특정 컬러 영역을 추출할 떄는 HSV 색 공간을 이용하는게 좋다.
RGB는 어두운 사진에서는 추출이 잘 되지 않는데,
HSV는 H,S로 색상을 조절하고 V는 밝기를 조절하기 때문에 H,S 범위만 지정해주면 어두운 사진이어도 추출할 수 있다.
따라서, BGR -> HSV 로 전환하고 컬러 영역 추출 해야 한다.
'''

import sys, cv2, numpy as np

src = cv2.imread('./images/candies.png')
src2 = cv2.imread('./images/candies2.png')

if src is None:
    print('Image load failed')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
src_hsv2 = cv2.cvtColor(src2, cv2.COLOR_BGR2HSV)

## RGB를 이용한 컬러 영역 추출
dst1 = cv2.inRange(src, (0,128,0), (100,255,100))
dst1_1 = cv2.inRange(src2, (0,128,0), (100,255,100)) # 최소(시작지점),최대(끝지점) 범위 지정
# B = 0~100, G = 128~255, R = 0~100 까지로 범위 지정
# 초록색 영역(rgb색공간 이미지에서 각자 좌표로 찍어서 보면 초록색영역쪽이다.)

## HSV를 이용한 컬러 영역 추출
dst2 = cv2.inRange(src_hsv, (50,150,0),(80,255,255))
dst2_1 = cv2.inRange(src_hsv2, (50,150,0),(80,255,255))
# 초록색 영역(hsv색공간 이미지에서 원에서 초록색 영역 각도.)
# 50 < h < 80 (초록색 영역)
# 150 < s < 255 (가운데는 탁하니까 바깥 부분만)
# 0 < v < 255 (밝기는 상관X)

cv2.imshow('src', src)
cv2.imshow('dst1', dst1) # hsv보다 더 깔끔하게 색상을 추출한다. 
# 근데 왜 영상처리할 떄는 RGB를 잘 안쓸까? 밝기가 어두워지면 추출을 잘 못함.
cv2.imshow('dst1_1', dst1_1) # 밝기가 어두워진 이미지 -> hsv보다 추출을 더 못함.
cv2.imshow('dst2', dst2)
cv2.imshow('dst2_1', dst2_1) # 밝기와 상관없이 동일하게 추출한다.

cv2.waitKey()
cv2.destroyAllWindows()