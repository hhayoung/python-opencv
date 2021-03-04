import sys
import numpy as np
import cv2


# 입력 영상 & 템플릿 영상 불러오기
# src = cv2.imread('./images/circuit2.bmp', cv2.IMREAD_GRAYSCALE)
# src = cv2.imread('./images/circuit3.bmp', cv2.IMREAD_GRAYSCALE)
# src = cv2.imread('./images/baseball_logo1.png', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('./images/baseball_logo2.png', cv2.IMREAD_GRAYSCALE)

# templ = cv2.imread('./images/crystal.bmp', cv2.IMREAD_GRAYSCALE)
# templ = cv2.imread('./images/baseball_patch1.png', cv2.IMREAD_GRAYSCALE)
templ = cv2.imread('./images/baseball_patch2.png', cv2.IMREAD_GRAYSCALE)

if src is None or templ is None:
    print('Image load failed!')
    sys.exit()

noise = np.zeros(src.shape, np.int32) # 잡음 추가

# cv2.Randn(dst, Scalar mean, Scalar stddev)
# 평균값 mean, 표준편차 stddev 를 분포로하는 이미지를 dst에 출력
cv2.randn(noise, 50, 10) # 밝기(50) 추가. sigma값 10  -> 밝기에 영향 없다고 했으니까 일부러 추가

src = cv2.add(src, noise, dtype=cv2.CV_8UC3) # 원본에 잡음 추가

# 출력값의 범위는 -1 ~ 1, 실수형 행렬
res = cv2.matchTemplate(src, templ, cv2.TM_CCOEFF_NORMED)
# 이 범위를 0(최소값) ~ 255(최대값)의 범위로 scaling
res_norm = cv2.normalize(res, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
# 현재 res는 -1~1 이니까 눈으로 확인할 때 편하게 보기 위해서 0~255로 범위를 맞춰준 것.

# 템플릿 매칭 결과가 나오면 cv2.minMaxLoc() 함수를 이용해 R(x,y)의 최대값 및 최소값과 그 위치를 얻을 수 있다
# 여기서는 cv2.TM_CCOEFF_NORMED를 사용했기 때문에 최대값만 가져오는 것
# minimum value, maximum value, minimum location, maximum location 리턴
_, maxv, _, maxloc = cv2.minMaxLoc(res)
# minv, _, minloc, _ = cv2.minMaxLoc(res) # cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED 을 사용할 때 필요
print('maxv:', maxv)
print('maxloc:', maxloc)

th, tw = templ.shape[:2]
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
cv2.rectangle(dst, maxloc, (maxloc[0] + tw, maxloc[1] + th), (0, 0, 255), 2)
# cv2.rectangle(dst, minloc, (minloc[0] + tw, minloc[1] + th), (0, 0, 255), 2)

cv2.imshow('templ',templ)
# cv2.imshow('res', res)
cv2.imshow('res_norm', res_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()