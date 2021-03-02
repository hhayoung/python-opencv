## 모폴로지 침식 연산 함수
# cv2.erode(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)
# src: 입력영상
# kernel: 구조 요소(structuring element), 커널 생성 함수: getStructuringElement()에 의해 생성
#         만약 None을 지정하면 3x3 사각형 구성 요소를 사용.
# anchor: 고정점 위치, 기본값(-1,-1) 이용하면 자동으로 중앙점이 설정됨
# iterations: 반복횟수, 기본값은 1
# borderType: 가장자리 픽셀 확장방식, 기본값은 cv2.BORDER_CONSTANT
# borderValue: cv2.BORDER_CONSTANT인 경우, 확장된 가장자리 픽셀을 채울 값을 정할 수 있다.

## 모폴로지 팽창 연산 함수
# cv2.dilate(src, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)
# erode와 파라미터는 같다.

## 모폴로지 구조 요소(커널) 생성하는 함수
# cv2.getStructuringElement(shape, ksize, anchor=None) => retval
# shape: 커널의 모양을 표현하는 플래그(cv2.MORPH_RECT(많이사용), cv2.MORPH_CROSS, cv2.MORPH_ELLIPSE(원에 들어오는 사각형))
# ksize: 커널의 크기(width,height) 튜플로 표현
# anchor: (-1,-1)
# retval: numpy.ndarray(0과 1로 구성된 값, 1의 위치가 커널의 모양을 결정함. 타입은 cv2.CV_8U)

import cv2, sys, numpy as np

src = cv2.imread('./images/circuit.bmp', cv2.IMREAD_GRAYSCALE)
if src is None:
    print("Image load failed")
    sys.exit()

# se = cv2.getStructuringElement(cv2.MORPH_RECT, (5,3))
# dst1 = cv2.erode(src, se)
# dst2 = cv2.dilate(src, None)

# 특별한 경우에 커널을 조정해서 사용할 수 있다.
se = cv2.getStructuringElement(cv2.MORPH_RECT, (1,6)) # 상하 수직선을 이어주고 싶을 때는 height값 더 주기
dst2 = cv2.dilate(src, se)

cv2.imshow('src', src)   # 원본에 끊어진 회로를 연결하고 싶어서 팽창을 했더니
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2) # 전체적으로 회로도가 다 굵어지고, 결국 연결이 안 된 곳도 있음. -> 커널 사이즈 조정
cv2.waitKey()

cv2.destroyAllWindows()