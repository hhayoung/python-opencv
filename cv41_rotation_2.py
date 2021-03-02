import sys, cv2, numpy as np

# 영상의 회전 변환 행렬(2 x 3) 구하는 함수
# cv2.getRotationMatrix2D(center, angle, scale)
# center : 회전 중심 좌표
# angle : 회전 각도(degree, 반시계방향), 음수는 시계방향
# scale : 확대 비율
# -> 회전행렬과 관련된 변환행렬(affine행렬)을 얻을 수 있다.

src = cv2.imread('./images/img_1.png')
if src is None:
    print('Image load failed')
    sys.exit()


# src이미지에서 중심점 구하기
center_pt = (src.shape[1]/2, src.shape[0]/2)

# aff 변환행렬 구하기
aff_arr = cv2.getRotationMatrix2D(center_pt, 45, 1)  # 반시계방향
# aff_arr = cv2.getRotationMatrix2D(center_pt, -45, 1) # 시계방향

dst = cv2.warpAffine(src, aff_arr, (0,0), borderMode=cv2.BORDER_CONSTANT, borderValue=(0,255,255))
# borderMode : cv2.BORDER_CONSTANT(기본값)
# borderValue : cv2.BORDER_CONSTANT일 때, borderValue를 바꿀 수 있다.

cv2.imshow('src',src)
cv2.imshow('dst',dst) # 원점중심으로 반시계방향으로 1radian 회전됨.
cv2.waitKey()

cv2.destroyAllWindows()