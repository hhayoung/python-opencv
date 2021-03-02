# Canny edge 검출 함수
# cv2.Canny(image, threshold1, threshold2, edge=None, apertureSize=None, L2gradient=None)
# image : 입력영상
# threshold1 : 하단임계값, threshold2 : 상단임계값 (보통 1:2 또는 1:3 비율을 사용한다)
# -> 상단임계값만 설정하면 보통 하단임계값은 1/2로 자동 설정된다.
# apertureSize : 소벨연산용 커널 크기, 기본값은 3
# L2gradient : True 이면 L2 norm 이용, False 이면 L1 norm 이용, 기본값은 False
# L2 norm 은 제곱이 들어가서 연산이 복잡, L1 norm 은 절대값 계산

import sys, cv2, numpy as np

# src = cv2.imread('./images/bd.png', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('./images/bd2.jpg', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed')
    sys.exit()

dst = cv2.Canny(src, 50, 150) # 1:3 비율
dst = cv2.Canny(src, 100, 150)
# 하단값을 높이면 짤리는 부분이 생김.
dst = cv2.Canny(src, 50, 200)
# 상단값을 높이면 하단값을 높인것보다는 덜 잘리지만 1:3 비율보다는 잘린다.


cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()

cv2.destroyAllWindows()