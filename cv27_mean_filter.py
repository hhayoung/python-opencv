# 기본적인 2d 필터링

# cv2.filter2D(src, ddepth, kernel, dst, anchor, delta, borderType)
# src : 입력영상, ddepth : 출력영상 데이터타입(cv2.CV_8U, cv2.CV_32F, cv2.CV_64F)
# kernel : 필터 마스크 행렬(실수형), anchor : (-1,-1) 이면 중앙점을 anchor로 사용하겠다는 의미
# 3x3인 경우 1,1이 들어가는게 맞는데 5x5에서는 2,2
# (-1,-1)로 하면 알아서 계산해서 중앙점을 골라준다. 
# delta : 추가적으로 더할 값, borderType : 가장자리 픽셀을 확장하는 방식

# cv2.blur(src, ksize)
# src : 입력영상, ksize : 평균 필터크기(weight, height) 튜플형태

'''
지금까지 계속 uint8로만 했었는데 필터링 연산을 할 때는 float형으로 해야 함.
numpy 계산할 때 보통 실수값을 이용해서 연산계산을 하는 이유는 
블러처리를 했을 때 -> 해당값이 딱딱 정수로 떨어지지 않고 소수점으로 결과값이 나온다. 
그 중간과정에서 소수점연산을 해줘야지만 그 미세한 부분의 결과값을 손실시키지 않고 가져올 수 있음.
중간중간 처리과정은 모두 float로 하고, 나중에 우리가 볼 때 맨 마지막에만 uint8로 바꿔줌
'''

import cv2, sys, numpy as np

src = cv2.imread('./images/rose.png', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed')
    sys.exit()

# 평균 필터
# kernel = np.array([[1/9, 1/9, 1/9],
#                    [1/9, 1/9, 1/9],
#                    [1/9, 1/9, 1/9]], dtype=np.float32)

kernel = np.ones((3,3), dtype=np.float64) / 9.

# 사용방법 2가지 > cv2.filter2d(), cv2.blur()

# dst = cv2.filter2D(src, -1, kernel) # ddepth = -1 은 입력영상과 동일한 타입으로 만들겠다는 의미

# cv2.blur(src, ksize) # ksize : 평균 필터 크기(weight, height) 튜플 형태로
# 내부적으로 kernel = np.ones((3,3), dtype=np.float64) / 9. 이렇게 계산됨.
dst = cv2.blur(src, (3,3))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()