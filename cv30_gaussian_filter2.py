# cv2.GaussianBlur(src, ksize, sigmaX, dst, sigmaY, borderType)
# src : 입력 영상, ksize : 가우시안 커널크기(0,0)으로 지정하면 sigmaX값에 의해서 자동으로 결정
# sigmaX : x방향의 sigma, sigmaY : y방향의 sigma. 0이면 sigmaX와 동일하게 설정됨

import cv2, sys, numpy as np

src = cv2.imread('./images/rose.png', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed')
    sys.exit()

cv2.imshow('src', src)

for sigma in range(1,6):
    dst = cv2.GaussianBlur(src, (0,0), sigma)

    desc = 'sigma: {}'.format(sigma)
    cv2.putText(dst, desc, (10,30), cv2.FONT_HERSHEY_TRIPLEX, 1.0, 255, 1, cv2.LINE_AA)

    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()