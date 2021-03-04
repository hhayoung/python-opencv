import sys
import numpy as np
import cv2

# 영상 불러오기
# obj = cv2.imread('./images/heart.png', cv2.IMREAD_GRAYSCALE)
obj = cv2.imread('./images/space.png', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('./images/symbols2.bmp', cv2.IMREAD_GRAYSCALE)

if src is None or obj is None:
    print('Image load failed!')
    sys.exit()

# 객체의 영상 외곽선 검출
# 반전을 통한 이진화 처리
_, obj_bin = cv2.threshold(obj, 128, 255, cv2.THRESH_BINARY_INV) # 이진화(객체추출을 위해 반전 필요)
obj_contours, _ = cv2.findContours(obj_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 외곽선 검출
obj_pts = obj_contours[0] # 외곽선 좌표들

# 입력 영상 분석
_, src_bin = cv2.threshold(src, 128, 255, cv2.THRESH_BINARY_INV) # 이진화
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 외곽선 검출

# 결과 영상
dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

# 입력 영상의 모든 객체 영역에 대해서
for pts in contours: # 각각의 외곽선
    if cv2.contourArea(pts) < 1000: # 노이즈 제거
        continue

    rc = cv2.boundingRect(pts) # 사각형 반환 -> (x, y, w, h)
    cv2.rectangle(dst, rc, (255, 0, 0), 1)

    # 모양 비교
    dist = cv2.matchShapes(obj_pts, pts, cv2.CONTOURS_MATCH_I3, 0)
    # distance 거리값이 리턴된다. 
    # dist값이 클수록 차이가 크므로 관련이 없고, dist값이 작을수록 비슷하다.

    # 사각형의 (x,y-3)의 좌표에 글씨를 쓰겠다.
    cv2.putText(dst, str(round(dist, 4)), (rc[0], rc[1] - 3),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1, cv2.LINE_AA)

cv2.imshow('obj', obj)
cv2.imshow('dst', dst)
cv2.waitKey(0)
