# 기본적인 2d 필터링

# cv2.filter2D(src, ddepth, kernel, dst, anchor, delta, borderType)
# src : 입력영상, ddepth : 출력영상 데이터타입(cv2.CV_8U, cv2.CV_32F, cv2.CV_64F)
# kernel : 필터 마스크 행렬(실수형), anchor : (-1,-1) 이면 중앙점을 anchor로 사용하겠다는 의미
# delta : 추가적으로 더할 값, borderType : 가장자리 픽셀을 확장하는 방식

import cv2, sys, numpy as np

src = cv2.imread('./images/rose.png', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed')
    sys.exit()

cv2.imshow('src', src)

# 커널 사이즈 5x5, 7x7 -> 블러효과가 커짐.
for ksize in (3,5,7):
    dst = cv2.blur(src, (ksize, ksize))

    # Mean 필터의 퀄리티는 좋은 편이 아니다.
    desc = 'Mean: {} x {}'.format(ksize, ksize)
    cv2.putText(dst, desc, (10,30), cv2.FONT_HERSHEY_TRIPLEX, 1.0, 255, 1, cv2.LINE_AA)

    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()