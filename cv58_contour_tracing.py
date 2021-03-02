# 외곽선 검출하기
import cv2, sys, numpy as np
import random

src = cv2.imread('./images/contours.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# cv2.RETR_EXTERNAL,cv2.RETR_LIST,cv2.RETR_TREE,cv2.RETR_CCOMP
contours, hier = cv2.findContours(src, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

print(len(contours)) # 9
print(hier)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

idx = 0 # 외곽선개수
while idx >= 0:
    # print(idx)

    # 색 지정(랜덤)
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # 계층정보를 입력했기 때문에 계층의 외곽선도 같이 그려준다. 그래서 계층끼리는 같은 색
    cv2.drawContours(dst, contours, idx, c, 2, cv2.LINE_8, hier)

    # print(hier[0,idx,0]) # 0번째 인덱스 외곽선의 next값을 가져옴
    idx = hier[0, idx, 0] #hierarchy의 shape=(1,N,4) N:외곽선개수
    # 더이상 외곽선이 없으면 -1이 리턴됨. -> while문 빠져나올 수 있음.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()