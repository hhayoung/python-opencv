# 영상 다운 샘플링
# cv2.pyrDown(src, dst, dstsize, borderType)
# src: 입력영상, dst: 출력영상 
# dstsize: 출력영상크기, 따로 설정하지 않는 경우 입력영상의 가로,세로 1/2크기로 설정

import sys, cv2, numpy as np

src = cv2.imread('./images/dog_img.png')
if src is None:
    print("Image load failed")
    sys.exit()

# 강아지 얼굴에만 사각형 그리기
rc = (220,110,150,150) # (x,y,w,h)
cpy = src.copy() # 복사본. 원본은 건드리는거 아님
cv2.rectangle(cpy, rc, (0,0,255), 2)
cv2.imshow('src_origin',cpy)
cv2.waitKey()

for i in range(1,4):
    src = cv2.pyrDown(src) # 총 3번 줄어든다.
    cpy = src.copy()

    cv2.rectangle(cpy, rc, (0,0,255), 2, shift=i) # shift=i를 주게 되면, 사이즈가 줄어들 때 사각형이 따라서 줄어든다.
    cv2.imshow('src',cpy)
    cv2.waitKey()
    cv2.destroyWindow('src') # 다음 for문을 돌릴 때 이전창의 잔상을 없애기 위해서는 for문이 끝날 때마다 해당 창을 닫아줌.

cv2.destroyAllWindows()