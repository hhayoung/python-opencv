# 오츠알고리즘
import cv2, sys, numpy as np

# src = cv2.imread('./images/sudoku.jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('./images/rice.png', cv2.IMREAD_GRAYSCALE)
if src is None:
    print("Image load failed")
    sys.exit()

# 오츠에 의한 전역 이진화
_, dst1 = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 지역 이진화 
dst2 = np.zeros(src.shape, np.uint8) # 지역 이진화해서 넣어줄 캔버스 만들어놓기

bw = src.shape[1] // 4  # 4등분
bh = src.shape[0] // 4  # 4등분 -> 더 많은 등분을 할 수록 더 깔끔한 결과가 나온다.

for y in range(4):
    for x in range(4):
        src_ = src[y*bh:(y+1)*bh, x*bw:(x+1)*bw] # 16등분해서 그 각 부분을 가져온 것.
        dst_ = dst2[y*bh:(y+1)*bh, x*bw:(x+1)*bw] # 캔버스의 분할된 부분

        # dst_를 파라미터로 사용하면 입력 및 출력으로 사용할 수 있다.
        cv2.threshold(src_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)
        # 그동안 앞에서는 결과영상은 생략했음. 파라미터로 쓰면 입력으로도 받고, 출력도 할 수 있음
        # dst = 이렇게 하고 사용해버리면 dst_ 정보가 사라져버린다.

        # -> 16등분해서 가져온 각각의 부분마다 다른 임계값을 갖게 되서 더 좋은 효과를 얻을 수 있다.

cv2.imshow('src',src)
cv2.imshow('dst1',dst1) # 전역 이진화
cv2.imshow('dst2',dst2) # 지역 이진화
cv2.waitKey()

cv2.destroyAllWindows()