## 허프변환에 의한 직선 검출
# cv2.HoughLines(image, rho, theta, threshold, lines=None, srn=None, stn=None, min-theta=None, max-theta=None) => lines
# image : 에지 입력 영상(Canny 연산을 이용한 에지 영상)
# rho(로우) : 축적 배열에서 rho 값의 간격(보통 1.0 사용)
# theta(세타) : 축적 배열에서 theta 값의 간격(보통 np.pi/180)

# rho, theta 값이 커지면 축적배열의 크기는 작아지고, 값이 작으면 축적배열은 커진다.
# 축적배열이 크면 정교한 직선을 표현할 수 있으나, 연산량이 많아진다.
# 축적배열이 작아면 정밀한 직선을 표현할 수 없으나, 연산량이 적어 속도는 빠르다.

# threshold : 축적배열에서 직선으로 판단할 임계값(임계값을 낮추면 많은 직선 검출, 반대로 높이면 검출되는 직선은 줄어든다.

# lines : rho, theta 값을 담고 있는 3차원 행렬(numpy.ndarray) 형태로 리턴된다.
# rho, theta를 행렬로 표현한다고 하면 rho, theta 2개만 있으면 되는데
# c++에서 파이썬으로 넘어오면서 쓸데없는 값이 추가되었다.
# lines 의 shape은 (N, 1, 2), dtype = numpy.float32 **shape 주의할 것
# 가운데 1이 의미없는 값. 그래서 나중에 코드화할 때 [0]을 집어넣으면 된다.

# rho, theta값은 우리가 알아보기 힘들다.
## 확률적 허프 변환
# cv2.HoughLinesP(image, rho, theta, threshold, lines=None, minLineLength=None, maxLineGap=None)
# image : 에지 입력 영상(Canny 연산을 이용한 에지 영상)
# rho(로우) : 축적 배열에서 rho 값의 간격(보통 1.0 사용)
# theta(세타) : 축적 배열에서 theta 값의 간격(보통 np.pi/180)
# threshold : 축적배열에서 직선으로 판단할 임계값(임계값을 낮추면 많은 직선 검출, 반대로 높이면 검출되는 직선은 줄어든다.

# lines : 선분의 시작과 끝 좌표(x1, y1, x2, y2) 정보를 담고 있는 numpy.ndarray
# shape=(N, 1, 4), dtype = numpy.int32

# minLineLength : 검출하기 위한 선분의 최소 길이. (최소길이에 못미치면 검출X)
# maxLineGap : 직선으로 간주하기 위한 최대 에지 점 간격. 기본값 0
# 기본값이 0일 때는, _ _ 이렇게 에지에 간격이 있으면 하나의 직선으로 보지 않고,
# 이 값을 4로 줬을 때는, __ _ __ ___ 이렇게 간격이 3개 있어도 하나의 직선으로 본다.

import sys, cv2, numpy as np

# src = cv2.imread('./images/bd.png', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('./images/bd2.jpg', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed')
    sys.exit()

edges = cv2.Canny(src, 50, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi/180.0, 150, minLineLength=50, maxLineGap=5) # threshold값 ↑적게검출 ↓많이검출 

# 색을 칠해서 선분을 표현할 거니까 해당 edge를 BGR로 바꿔줘야함. Canny()하면 grayscale됨.
dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

if lines is not None:
    for i in range(lines.shape[0]): # N개 검출됨. N의 값은 알 수 없다.
        pt1 = (lines[i][0][0], lines[i][0][1]) # 시작점 좌표, 가운데 값은 무조건 0으로
        pt2 = (lines[i][0][2], lines[i][0][3]) # 끝점 좌표, 가운데 값은 무조건 0으로

        cv2.line(dst, pt1, pt2, (0,255,0), 2, cv2.LINE_AA)


cv2.imshow('src',src)
cv2.imshow('edges',edges)
cv2.imshow('dst',dst)
cv2.waitKey()

cv2.destroyAllWindows()