# threshold (임계값 함수)
# cv2.threshold(src, thresh, maxval, type, dst) => retval, dst 2가지 리턴
# src: 입력영상, thresh: 사용자가 지정한 임계치
# maxval: 무조건 255(임계값 최대치기 때문에)
# type: 기본적으로 cv2.THRESH_BINARY, CV2.THRESH_BINARY_INV(inverse) 이 두 가지 타입이 대부분 사용됨.
# retval: 사용자가 지정한 임계값
# dst: 출력영상

import cv2, sys, numpy as np

# src = cv2.imread('./images/cell_4.jpg', cv2.IMREAD_GRAYSCALE)
# src = cv2.imread('./images/rice.png', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('./images/sudoku.jpg', cv2.IMREAD_GRAYSCALE)
if src is None:
    print("Image load failed")
    sys.exit()

# ***주의! 리턴값이 2개
# dst = cv2.threshold(src, 200, 255, cv2.THRESH_BINARY) # 영상 출력이 되지 않는다.
# _, dst = cv2.threshold(src, 200, 255, cv2.THRESH_BINARY) # 적혈구까지
# _, dst = cv2.threshold(src, 140, 255, cv2.THRESH_BINARY) # 백혈구 핵만


def on_trackbar(pos):
    thresh = cv2.getTrackbarPos('thresh', 'dst')
    _, dst = cv2.threshold(src, thresh, 255, cv2.THRESH_BINARY)
    # 또는 바로 pos 값 넣기도 가능
    # _, dst = cv2.threshold(src, pos, 255, cv2.THRESH_BINARY)
    cv2.imshow('dst', dst)

# 트랙바 생성
cv2.namedWindow('dst')
cv2.createTrackbar('thresh', 'dst', 0, 255, on_trackbar)
cv2.setTrackbarPos('thresh', 'dst', 100)
cv2.waitKey()

# cv2.imshow('src',src)
# cv2.imshow('dst',dst)
# cv2.waitKey()

cv2.destroyAllWindows()