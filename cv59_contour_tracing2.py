# 우유가 떨어지는 이미지의 외곽선 검출하기
import cv2, sys, numpy as np
import random

src = cv2.imread('./images/milkdrop.bmp', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed!')
    sys.exit()

# 전역이진화(흰,검만 있는 이미지로 만들기 위해서)
_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# cv2.RETR_EXTERNAL,cv2.RETR_LIST,cv2.RETR_TREE,cv2.RETR_CCOMP
contours, hier = cv2.findContours(src_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# print(len(contours)) # 9
print(hier)

h, w = src.shape[:2]
dst = np.zeros((h,w,3), np.uint8)  # 검은색화면에 윤곽선을 나타내고 싶을 때
# dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)   # 원본 이미지에 윤곽선을 나타내고 싶을 때

## hierarchy 를 이용한 방법
# idx = 0 # 외곽선개수
# while idx >= 0:
#     # 색 지정(랜덤)
#     c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
#     cv2.drawContours(dst, contours, idx, c, 1, cv2.LINE_8) 

#     print(hier[0,idx,0]) # 0번째 인덱스 외곽선의 next값을 가져옴
#     idx = hier[0, idx, 0] #hierarchy의 shape=(1,N,4) N:외곽선개수
#     # 더이상 외곽선이 없으면 -1이 리턴됨. -> while문 빠져나올 수 있음.

## contours 를 이용한 방법
# N개의 contours만큼 반복
for i in range(len(contours)):
    # 색 지정(랜덤)
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst, contours, i, c, 1, cv2.LINE_8, hier) # hier값 : 계층정보 넣어줄 때 넣고, 아니면 생략


cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()