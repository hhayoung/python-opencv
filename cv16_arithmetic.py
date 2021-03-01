# 산술 연산

# cv2.add, cv2.subtract, cv2.addWeighted, cv2.absdiff

import sys, cv2, numpy as np

src1 = cv2.imread('./images/lenna256.bmp',)
src2 = cv2.imread('./images/square.bmp',)
src3 = cv2.imread('./images/hole.bmp',)

# 더하기 연산
dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U) 
# src2의 검은색부분은 0, 흰색부분은 255.
# 그렇기 때문에 검은색부분은 값이 더해지지않아서 그대로 나오고, 흰색은 더해서 255가 넘기 때문에 saturate연산이 되어 255가 되어 흰색이 출력된다.

# cv2.addWeighted(src1, alpha, src2, beta, gamma, dst, dtype)
# src1  : 첫번째 영상, src2: 두번째 영상
# alpha : 첫번째 영상의 가중치
# beta  : 두번째 영상의 가중치
# gamma : 결과 영상에 추가적으로 더해줄 값
# dst   : 리턴값이 dst기 때문에 거의 생략한다.
# dtype : 출력영상(dst) 타입
dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0) # 둘 다 반투명이라서 둘 다 보이는 것.
dst3 = cv2.subtract(src1,src2) # saturate연산으로 0이 되어 검은색 나옴.

# cv2.absdiff(src1, src2, dst) : | src1 - src2 |
# : 두 영상의 같은 위치에 존재하는 픽셀 값에 대하여 뺼셈 연산을 수행한 후, 그 절대값을 결과 영상의 픽셀 값으로 반영
dst4 = cv2.absdiff(src1,src2) # src1 - 255를 뺀 값을 절대값 => 차이. 그 차이값을 반영한 것

cv2.imshow('dst1',dst1)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.imshow('dst4',dst4)

dst11 = cv2.add(src1, src3, dtype=cv2.CV_8U)
dst22 = cv2.addWeighted(src1,0.5,src3,0.5,0.0)
dst33 = cv2.subtract(src1, src3)
dst44 = cv2.absdiff(src1, src3)

cv2.imshow('dst11',dst11)
cv2.imshow('dst22',dst22)
cv2.imshow('dst33',dst33)
cv2.imshow('dst44',dst44)


cv2.waitKey()
cv2.destroyAllWindows()
