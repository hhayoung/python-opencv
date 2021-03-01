# cv2.GaussianBlur(src, ksize, sigmaX, dst, sigmaY, borderType)
# src : 입력 영상, ksize : 가우시안 커널크기(0,0)으로 지정하면 sigmaX값에 의해서 자동으로 결정
# sigmaX : x방향의 sigma, sigmaY : y방향의 sigma. 0이면 sigmaX와 동일하게 설정됨

import cv2, sys, numpy as np

src = cv2.imread('./images/rose.png', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed')
    sys.exit()

 # 블러를 더 주고자 할 때는 2,3으로 입력(값이 커질수록 연산량 증가)
dst = cv2.GaussianBlur(src, (0,0), 1) # 시그마가 1일 때는 uint8에서 mean(7, 7) -> 6σ+1이니까
# dst = cv2.GaussianBlur(src, (0,0), 2) # 블러 효과 ↑

# 평균값 필터와 비교
dst2 = cv2.blur(src, (7,7)) # 평균값필터가 더 뭉개져서 보임. 블러 질이 안좋음.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()