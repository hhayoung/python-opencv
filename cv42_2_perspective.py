# Rotation하고 투시변환하기 vs 바로 투시변환하기 
# 뭐가 더 화질 좋은지 테스트 해보기

import sys, cv2, numpy as np

src = cv2.imread('./images/name_card_3.jpg')

## Rotation하고 투시변환
# 중심점
center_pt = (src.shape[1]/2, src.shape[0]/2)
# 변환행렬
aff_arr = cv2.getRotationMatrix2D(center_pt, -110, 1)
# 회전
dst = cv2.warpAffine(src, aff_arr, (0,0))
# 투시변환
w, h = 720, 400
# 소스좌표
src_Coord = np.array([[246,221],[650,286],[692,518],[253,550]], dtype=np.float32)
# 출력 좌표
dst_Coord = np.array([[0,0],[w-1,0],[w-1,h-1],[0,h-1]], dtype=np.float32)
# 투시변환행렬
per_matrix = cv2.getPerspectiveTransform(src_Coord, dst_Coord)

rot_per_dst = cv2.warpPerspective(dst, per_matrix, (w,h))

## 바로 투시변환
w, h = 720, 400
# 소스좌표
src_Coord2 = np.array([[428,630],[351,226],[555,108],[734,510]], dtype=np.float32)
# 출력 좌표
dst_Coord2 = np.array([[0,0],[w-1,0],[w-1,h-1],[0,h-1]], dtype=np.float32)
# 투시변환행렬
per_matrix2 = cv2.getPerspectiveTransform(src_Coord2, dst_Coord2)

per_dst = cv2.warpPerspective(src, per_matrix2, (w,h))


##### 샤프닝 : 글씨 더 선명하게 해주기
## Rotation하고 투시변환 -> 샤프닝
rot_per_dst_ycrcb = cv2.cvtColor(rot_per_dst, cv2.COLOR_BGR2YCrCb)
channels = cv2.split(rot_per_dst_ycrcb)
channels[0] = cv2.GaussianBlur(channels[0], (0,0), 2)
rot_per_dst_ycrcb_blur = cv2.merge(channels)
rot_per_dst_blur = cv2.cvtColor(rot_per_dst_ycrcb_blur, cv2.COLOR_YCrCb2BGR)
rot_per_dst_sharp = np.clip(2.0*rot_per_dst - rot_per_dst_blur, 0, 255).astype(np.uint8) # 훨씬 선명해짐

## 바로 투시변환 -> 샤프닝
per_dst_ycrcb = cv2.cvtColor(per_dst, cv2.COLOR_BGR2YCrCb)
channels = cv2.split(per_dst_ycrcb)
channels[0] = cv2.GaussianBlur(channels[0], (0,0), 2)
per_dst_ycrcb_blur = cv2.merge(channels)
per_dst_blur = cv2.cvtColor(per_dst_ycrcb_blur, cv2.COLOR_YCrCb2BGR)
per_dst_sharp = np.clip(2.0*per_dst - per_dst_blur, 0, 255).astype(np.uint8) # 훨씬 선명해짐

cv2.imshow('src', src)
cv2.imshow('rot_per_dst', rot_per_dst) # 회전시키고 투시변환
cv2.imshow('rot_per_dst_sharp', rot_per_dst_sharp) # 회전시키고 투시변환하고 샤프닝

cv2.imshow('per_dst', per_dst) # 투시변환
cv2.imshow('per_dst_sharp', per_dst_sharp) # 투시변환하고 샤프닝
cv2.waitKey()

cv2.destroyAllWindows()