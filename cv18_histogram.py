'''
# 히스토그램 (교재 p.99)
영상의 픽셀 값 분포를 그래프 형태로 표현한 것
'''
# 히스토그램 구하는 함수
# cv2.calcHist(images, channels, mask, histSize, ranges, hist=None, accumulate)
# images    : 입력 영상 리스트
# channels  : 히스토그램을 얻기 위한 채널 리스트
# mask      : 마스크 영상
# histSize  : bin의 개수(막대개수)를 나타내는 리스트
# ranges    : 히스토그램 각 차원의 최소, 최대값으로 구성된 리스트
# hist      : 계산된 히스토그램
# accumulate: 기존의 hist 히스토그램에 누적여부(True/False)

# 명암비(Contrast) : 어두운 곳과 밝은 곳의 밝기 차이(대비)

# 히스토그램 스트레칭(Histogram stretching)
# 영상의 히스토그램이 그레이스케일 전체에 걸쳐 나타나도록 변경하는 선형 변환 기법
# : 영상의 명암비를 자동으로 조절하는 기법
# 정규화 함수 : cv2.normalize(src, dst, alpha, beta, norm_type, dtype, mask)

# 히스토그램 평활화(Histogram equalization)
# : 히스토그램 평탄화, 전체 그레이스케일 구간에 히스토그램이 분포되도록 하는 명암비 향상 기법
# 함수 : cv2.equalizeHist(src, dst) => dst
# src   : 입력 영상, 그레이스케일 영상

import sys, cv2, numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

## 그레이스케일 [0], BG [0,1], BGR [0,1,2]
hist = cv2.calcHist([src], [0], None, [256], [0, 256]) # 꼭 리스트 형태로 입력
# hist = cv2.calcHist([이미지리스트], [채널리스트], mask=None, [bin개수], [범위])

cv2.imshow('src',src)
cv2.waitKey(10) # 10으로 설정한 이유: 다음 matplot 명령어 실행을 위해

plt.plot(hist)
plt.show()

## 컬러 영상 히스토그램
src = cv2.imread('./images/lenna.bmp')
if src is None:
    print('Image load failed')
    sys.exit()

# 컬러를 구분할 수 있는 리스트 필요
colors = [ 'b','g','r' ] # -> 각각의 채널에 해당되는 히스토그램을 만들어야 함.
bgr_channels = cv2.split(src)


'''
# zip() 
>>> a = [1,2,3]
>>> b = ['k','o','p']
>>> a_b = list(zip(a,b))
>>> print(a_b)
[(1, 'k'),(2, 'o'),(3, 'p')] 
-> 이런 식으로 값을 같이 받아와서 각각 channel과 c에 대입해준다.
'''
for (channel, c) in zip(bgr_channels, colors):
    hist = cv2.calcHist([channel], [0], None, [256], [0,256]) # 각 채널별로 히스토그램
    # hist 타입 : 1차원 행렬
    plt.plot(hist, color = c)

cv2.imshow('src',src)
cv2.waitKey(1)

plt.show()

cv2.destroyAllWindows()