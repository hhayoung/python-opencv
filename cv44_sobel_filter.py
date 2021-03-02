# sobel필터 사용해서 영상 미분 해보기
import sys, cv2, numpy as np

src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed')
    sys.exit()

# # sobel 필터(x방향)
kernel_x = np.array([[-1,0,1],
                   [-2,0,2],
                   [-1,0,1]], dtype=np.float32)

# x방향으로 편미분
dx = cv2.filter2D(src, -1, kernel_x, delta=128) # -1 = 입력영상과 똑같이 하겠다
# 갑자기 어두워지는 부분은 엣지로 검출이 X
# => 밝은색->어두운색 -값이 나오는데, -값일때는 saturation에 의해서 0으로 맞춰진것.
# 이 어두운 곳도 엣지인데 이 엣지변화량을 보고싶을 때는 어떻게 해야할까?
# 이걸 보고싶으면 결과값에다가 값을 추가해주면 됨.
# delta=128을 주면서 값을 추가해줬다. 이제 엣지부분 다 보임

# sobel 필터(y방향)
kernel_y = np.array([[-1,-2,-1],
                     [0,0,0],
                     [1,2,1]], dtype=np.float32)
# y방향으로 편미분
dy = cv2.filter2D(src, -1, kernel_y, delta=128)

# sobel 필터 함수
# cv2.Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None)
# src : 입력영상, ddepth : 출력영상의 데이터타입(-1이면 입력영상과 같음) - cv2.CV_32F로 연산하는 것이 일반적임.
# dx : x방향 미분차수, dy : y방향 미분차수(1차미분 또는 2차미분 지정)
# 일반적으로는 1차미분, dx=1, dy=0으로 또는 dx=0, dy=1로 설정하는 것이 일반적임.
# ksize : 보통 3으로 지정
# scale : 연산결과에 추가적으로 곱할 값(기본값 1)
# delta : 연산결과에 추가적으로 더할 값(기본값 0)
# borderType : 가장자리 픽셀 확장 방식, 기본값은 cv2.BORDER_DEFAULT 

# scharr(샤르) 필터 함수(파라미터는 소벨과 동일)
# cv2.Sharr(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None)

# 소벨필터이용
dx = cv2.Sobel(src, -1, 1, 0, delta=128)
dy = cv2.Sobel(src, -1, 0, 1, delta=128)

cv2.imshow('src', src)
cv2.imshow('dx', dx) # x방향으로 미분했을 때, 가장 변화량이 큰 부분이 엣지로 검출됨.
cv2.imshow('dy', dy)
cv2.waitKey()

cv2.destroyAllWindows()