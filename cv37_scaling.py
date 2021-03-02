import cv2, sys, numpy as np

src = cv2.imread('./images/rose.bmp') # src.shape(320, 480, 3)
if src is None:
    print('Image load failed')
    sys.exit()

# 영상의 크기를 변환시킬 때 사용한 함수
# cv2.resize(src, dsize, dst, fx, fy, interpolation(보간법))
# src: 입력영상, dsize: 출력영상 크기(w,h) - (0,0)이면 fx, fy값을 이용하여 결정
# fx, fy : x와 y방향 스케일 비율(scale factor)

dst1 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
print(dst1.shape) # (1280, 1920, 3)
dst2 = cv2.resize(src, (1920, 1280))
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('src',src)
cv2.imshow('dst1',dst1[500:800,400:800]) # cv2.INTER_NEAREST -> 퀄리티 가장 안좋음.
cv2.imshow('dst2',dst2[500:800,400:800]) # cv2.INTER_LINEAR
cv2.imshow('dst3',dst3[500:800,400:800]) # cv2.INTER_CUBIC
cv2.imshow('dst4',dst4[500:800,400:800]) # cv2.INTER_LANCZOS4
# cv2.INTER_LINEAR vs cv2.INTER_CUBIC vs cv2.INTER_LANCZOS4
# -> 별 차이 없다. 월등히 화질이 더 좋고 그런게 아니기 때문에 그냥 cv2.INTER_LINEAR 를 사용한다. 
cv2.waitKey()

cv2.destroyAllWindows()