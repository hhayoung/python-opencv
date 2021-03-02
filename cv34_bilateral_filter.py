import cv2, sys, numpy as np

src = cv2.imread('./images/lenna.bmp')
if src is None:
    print('Image load failed')
    sys.exit()

# 양방향 필터링 함수
# cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace, dst, borderType)
# src : 입력영상, d : 필터링에 사용될 아웃픽셀의 거리(지름) -1을 설정해서 사용하는 것이 좋다.
# sigmaColor : 색공간에서의 필터 표준편차
# sigmaSpace : 좌표공간에서의 필터의 표준편차

# sigmaColor값이 커지면 전체적으로 블러링 되는 효과
# sigmaSpace 값이 5보다 크면 가우시안필터 사이즈가 커지므로 연산속도가 느려짐.
# dst = cv2.bilateralFilter(src, -1, 10, 5) # 피부부분을 보면 좀 더 매끄러워짐
dst = cv2.bilateralFilter(src, -1, 100, 50)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()

cv2.destroyAllWindows()