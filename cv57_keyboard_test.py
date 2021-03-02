import sys
import numpy as np
import cv2

src = cv2.imread('./images/key1.jpg', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed!')
    sys.exit()

# 출력영상만
_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)

# noise 제거 - 방법 1번째
# src_bin = cv2.morphologyEx(src_bin, cv2.MORPH_OPEN, None)

# 전체 객체 개수 + 1, stats 행렬(객체의 바운딩 박스 정보)
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

# 컬러 변환
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# 0번이 배경이라서 
# 배경을 제외하기 위해서 1부터 시작
for i in range(1, cnt):
    (x, y, w, h, area) = stats[i]

    print(area)
    # area(픽셀의 개수)를 이용한 noise 제외 - 방법 2번째
    if area < 30:
        continue

    # 두께 2픽셀로 사각형 그리기
    cv2.rectangle(dst, (x, y, w, h), (255, 0, 255), 2)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()