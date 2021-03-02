# 어파인 변환 행렬 구하기
# cv2.getAffineTransform(src, dst) => 리턴값 2 x 3 행렬
# 투시 변환 행렬 구하기
# cv2.getPerspectiveTransform(src, dst) => 리턴값 3 x 3 행렬
# 어파인변환 함수
# cv2.warfAffin(src, M, dsize, dst, flags, borderMode, borderValue)
# 투시변환 함수
# cv2.warfPerspective(src, M, dsize, dst, flag, borderMode, borderValue)

import sys, cv2, numpy as np

src = cv2.imread('./images/name_card_2.jpg')
if src is None:
    print('Image load failed')
    sys.exit()


# 일반 명함카드 비율 (9:5)
w, h = 400, 720

# 소스의 좌표
# 포토샵 창->정보 - 픽셀값x
# 편집 -> 환경설정 -> 단위와 눈금자 -> 눈금자를 픽셀로 변경
src_Coord = np.array([[143,275],[317,148],[693,330],[570,535]], dtype=np.float32)

# 출력 좌표
dst_Coord = np.array([[0,0],[w-1,0],[w-1,h-1],[0,h-1]], dtype=np.float32)

# 투시변환행렬
per_matrix = cv2.getPerspectiveTransform(src_Coord, dst_Coord)

per_dst = cv2.warpPerspective(src, per_matrix, (w,h))

##### 샤프닝 : 글씨 더 선명하게 해주기 
# YCrCb로 변환
dst_ycrcb = cv2.cvtColor(per_dst, cv2.COLOR_BGR2YCrCb)
# 채널 분리
channels = cv2.split(dst_ycrcb)
# Y채널만 블러처리
channels[0] = cv2.GaussianBlur(channels[0], (0,0), 2)
# 다시 합쳐줌
dst_ycrcb_blur = cv2.merge(channels)
dst_blur = cv2.cvtColor(dst_ycrcb_blur, cv2.COLOR_YCrCb2BGR)
dst = np.clip(2.0*per_dst - dst_blur, 0, 255).astype(np.uint8) # 훨씬 선명해짐


cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()

cv2.destroyAllWindows()