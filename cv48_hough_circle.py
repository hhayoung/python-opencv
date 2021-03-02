## 허프변환에 의한 원 검출 함수
# cv2.HoughCircles(image, method, dp, minDist, circles=None, param1=None, param2=None, minRadius=None, maxRadius=None)
# image : 일반 그레이스케일 입력 영상(에지 영상X), 에지영상에서는 방향성분을 알 수 없음.
# (edge영상이 들어가면 흰,검밖에 없으니까 방향성분을 구할 수가 없음.) 그래디언트 벡터계산을 해야하니까 
# 벡터 크기를 구할 수 있으니까 <- x,y 미분해줘야 하니까
# method : OpenCV 4.2 이하에서는 cv2.HOUGH_GRADIENT를 지정해야 함. (버전마다 조금씩 다름)
# dp : 축적배열의 크기 비율 (1넣으면 됨)
# minDist(minDistance) : 검출된 원의 중심점들의 최소거리
# circles : (cx, cy, r) 정보를 갖고 있는 np.ndarray, shape=(1, N, 3), dtype=np.float32  **직선검출에서의 shape과 다르니까 주의!
# param1 : Canny 에지 검출기의 높은 임계값
# param2 : 축적배열에서 원 검출을 하기 위한 임계값
## param1 값이 결정되면 낮은 임계치값은 자동으로 결정(1/2값으로)
## param2 값에 따라 많은 원이 검출될 수 있고, 원이 검출 안될 수 있음.
# minRadius : 검출할 원의 최소 반지름
# maxRadius : 검출할 원의 최대 반지름

import sys, cv2, numpy as np

# src = cv2.imread('./images/old_tel.png')
# src = cv2.imread('./images/old_tel2.png')
# src = cv2.imread('./images/coin.jpg')
# src = cv2.imread('./images/coin2.jpg')
# src = cv2.imread('./images/coin3.jpg')
# src = cv2.imread('./images/coin4.jpg')
# src = cv2.imread('./images/traffic_light.jpg')
# src = cv2.imread('./color_circle.jpg')
src = cv2.imread('./red.jpg')
# src = cv2.imread('./images/test_coin.jpg')
if src is None:
    print('Image load failed')
    sys.exit()

# 블러처리 해서 노이즈 제거하면 성능이 좋아짐.
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# -> 그레이스케일로 하는 이유 : 컬러일 때는 빛번짐이나 그런것들이 있어서 그런걸 제거하고 좀 더 선명한 걸 쓰기 위해
blur = cv2.GaussianBlur(gray, (0,0), 1.0)


def on_trackbar(pos):
    # 트랙바에서 각자 값 가져오기
    rmin = cv2.getTrackbarPos('minRadius', 'img')
    rmax = cv2.getTrackbarPos('maxRadius', 'img')
    th = cv2.getTrackbarPos('threshold', 'img')

    # 원검출
    # cv2.HoughCircles(image, method, dp, minDist, circles=None, param1=None, param2=None, minRadius=None, maxRadius=None)
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, param1=120, param2=th, minRadius=rmin, maxRadius=rmax)
    print(circles.shape)
    dst = src.copy()
    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = circles[0][i]
            cv2.circle(dst, (cx,cy), radius, (0,0,255), 2, cv2.LINE_AA)

    cv2.imshow('img', dst)


# 트랙바 생성
cv2.imshow('img',src)
cv2.createTrackbar('minRadius', 'img', 0, 100, on_trackbar)
cv2.createTrackbar('maxRadius', 'img', 0, 150, on_trackbar)
cv2.createTrackbar('threshold', 'img', 0, 100, on_trackbar)
cv2.setTrackbarPos('minRadius', 'img', 10)
cv2.setTrackbarPos('maxRadius', 'img', 80)
cv2.setTrackbarPos('threshold', 'img', 40)
cv2.waitKey()

cv2.destroyAllWindows()