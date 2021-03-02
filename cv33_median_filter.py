import cv2, sys, numpy as np

src = cv2.imread('./images/noise.bmp', cv2.IMREAD_GRAYSCALE)

# cv2.medianBlur(src, ksize, dst)
# src: 입력영상, ksize: 커널크기, dst: 출력영상

# 커널사이즈를 키울수록 노이즈는 사라지지만, 이미지가 뭉치는 현상이 발생함.
dst = cv2.medianBlur(src, 5)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()

cv2.destroyAllWindows()