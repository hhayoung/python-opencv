# 컬러 space
# 색 분리(채널 분리)
# cv2.split(m, mv) => dst
# m     : 다채널 영상(BGR)으로 구성된 컬러 영상
# mv    : 출력 영상 (보통 생략)
# dst   : 출력 영상 리스트

# 색결합(채널 결합)
# cv2.merge(mv, dst) => dst
# mv    : 입력 영상 리스트
# dst   : 출력 영상

## 영상처리에서는 특정 목적에 따라서 RGB 색공간(space)을 HSV, YCrCb, Grayscale 등의 색공간으로 전환해서 처리한다.
# 교재 p.75 컬러 공간 변환

import sys, cv2, numpy as np

src = cv2.imread('./images/candies.png')

print('src.shape:', src.shape) # (480, 640, 3)
print('src.dtype:', src.dtype) # uint8

b_channel, g_channel, r_channel = cv2.split(src) # bgr 순서대로 리스트가 넘어온다.

# cv2.imshow('src',src)
# cv2.imshow('b_channel',b_channel) # 파란색=하얗게 보인다.
# cv2.imshow('g_channel',g_channel) # 초록색=하얗게 보인다. 노란색은 초록색이 포함되어 있어서 하얗게 보인다.
# cv2.imshow('r_channel',r_channel) # 빨간색=하얗게 보인다. 노란색은 빨간색이 포함되어 있어서 하얗게 보인다. 

## 색 공간 변환 함수 : cv2.cvtColor(src, code, dst, dstCn) => dst
# src   : 입력 영상
# code  : 색 변환 코드
# dst   : 출력 영상
# dstCn : 결과 영상의 채널수

'''
# HSV 색공간
Hue : 색의 종류(무지개 색)
Saturation : 채도, 색이 탁한지 선명한지를 나타내는 정도
Value : 명도, 빛의 밝기
cv2.CV_8U일 때 HSV 값의 범위 : 0 <= H <= 179,  0 <= S, V <= 255


# YCrCb 색공간
PAL(유럽 주파수방식), NTSC(미국 주파수방식) 등의 컬러비디오 표준에 사용되는 색공간
Y: 밝기 정보(luma)
Cr, Cb: 색 차이(chroma)
cv2.CV_8U일 때 YCrCb 값의 범위 : 0 <= Y, Cr, Cb <= 255

'''

# hsv 스페이스로 변환
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
channels = cv2.split(src_hsv)

cv2.imshow('src',src)
cv2.imshow('channels[0]', channels[0])
cv2.imshow('channels[1]', channels[1])
cv2.imshow('channels[2]', channels[2])

cv2.waitKey()
cv2.destroyAllWindows()