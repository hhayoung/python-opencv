# 어파인 변환 행렬 구하기
# cv2.getAffineTransform(src, dst) => 리턴값 2 x 3 행렬

# 투시 변환 행렬 구하기
# cv2.getPerspectiveTransform(src, dst) => 리턴값 3 x 3 행렬

# 어파인변환 함수
# cv2.warfAffin(src, M, dsize, dst, flags, borderMode, borderValue)

# 투시변환 함수
# cv2.warfPerspective(src, M, dsize, dst, flag, borderMode, borderValue)

import sys, cv2, numpy as np

src = cv2.imread('./images/name_card.jpg')
if src is None:
    print('Image load failed')
    sys.exit()


# 일반 명함카드 비율 (9:5)
w, h = 720, 400

# 소스의 좌표
# 포토샵 창->정보 - 픽셀값x
# 편집 -> 환경설정 -> 단위와 눈금자 -> 눈금자를 픽셀로 변경
src_Coord = np.array([[228,115],[797,223],[747,563],[78,382]], dtype=np.float32)

# 출력 좌표
dst_Coord = np.array([[0,0],[w-1,0],[w-1,h-1],[0,h-1]], dtype=np.float32)

# 투시변환행렬
per_matrix = cv2.getPerspectiveTransform(src_Coord, dst_Coord)

dst = cv2.warpPerspective(src, per_matrix, (w,h))

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()

cv2.destroyAllWindows()