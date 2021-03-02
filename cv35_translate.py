import cv2, sys, numpy as np

src = cv2.imread('./images/img_1.png')
if src is None:
    print('Image load failed')
    sys.exit()

# 영상의 어파인 변환 함수
# cv2.warpAffine(src, M, dsize, dst, flags, borderMode, borderValue)
# src: 입력영상, M: 2x3어파인 변환행렬(실수형)
# dsize: 결과 영상의 크기(w,h) - (0,0)이면 입력영상과 같은 크기로 설정
# flags: 보간법(기본값은 cv2.INTER_LINEAR)을 설정하는 파라미터
# 보간법: 결과 영상의 퀄리티를 보정하는 방법(cv2.INTER_LINEAR가 기본값인데 가장 효율이 좋다.)
# cv2.INTER_NEAREST 
# cv2.INTER_LINEAR (효율성이 가장 높다. 퀄리티 및 속도 빠름)
# cv2.INTER_CUBIC 퀄리티는 더 좋은데 속도 느림 -> 퀄리티가 미친듯이 좋은건 아니라 linear 쓰는 것.
# cv2.INTER_LANCZOS4
# cv2.INTER_AREA : 영상 축소시 효과적으로 사용
# borderMode : cv2.BORDER_CONSTANT(기본값)
# borderValue : cv2.BORDER_CONSTANT일 때, borderValue를 바꿀 수 있다.


# 입력영상필요, 어파인 변환행렬필요

# aff = np.array([[1,0,a(가로이동크기)], [0,1,b(세로이동크기)]])
aff = np.array([[1,0,300], 
                [0,1,200]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0,0))

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()

cv2.destroyAllWindows()