# 2D 벡터 크기 구하는 함수
# cv2.magnitude(x, y, magnitude=None)
# x : 2D 벡터의 x좌표 행렬(실수형)               - x의 편미분
# y : 2D 벡터의 y좌표 행렬, x와 같은 크기(실수형) - y의 편미분

import sys, cv2, numpy as np

src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed')
    sys.exit()

# 각각의 편미분 실수형으로 계산
dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

# 한꺼번에 적용
mag_val = cv2.magnitude(dx, dy)
mag_val = np.clip(mag_val, 0, 255).astype(np.uint8) # saturation설정해주고, uint8로 변환

edge = np.zeros(mag_val.shape[:2], np.uint8)
edge[mag_val > 160] = 255  # mag_val=T값의 역할
# 기준이 낮을 수록 엣지 검출이 많고, 기준이 높을 수록 엣지 검출이 적다.
# 엣지의 두께를 얇게 검출하려면 T값을 높이면 된다. 그대신 엣지는 중간중간 짤린다.
# -> 해결 방법 Canny : 엣지를 얇게 검출하면서도 선이 끊기지 않게 검출하는 방법

cv2.imshow('src',src)
cv2.imshow('mag_val',mag_val)
cv2.imshow('edge',edge)
cv2.waitKey()

cv2.destroyAllWindows()