# 영상 화소 처리(Point processing)
# : 특정 좌표의 픽셀 값을 변경하여 출력 영상의 해당 좌표 픽셀값으로 설정

# np.uint8이면 
# 화소의 크기를 표현한다면 x, y축 0~255
# dst(x,y)(출력화소) = f(src(x,y))
# 이미지를 그대로 가져오려면 항등함수(일대일 직선 함수) 입력값이 들어오면 그대로 출력값으로 픽셀의 변화가 없도록
# 근데 밝기를 조절하고 싶다면 
# 밝게 -> 입력값에다가 +2를 해준거. y 절편 값이 있는 함수. 255를 넘어서는 안되기 때문에 255지점에서는 가로로
# 어둡게 -> - 해주면 됨. 0지점에서는 가로로 가다가 기울기가 시작된다.

# 밝기 조절 :  cv2.add(src1, src2, dst, mask, dtype)
# src1 : 첫번째 영상 또는 스칼라 값(입력)
# src2 : 두번째 영상 또는 스칼라 값(입력)
# dst : 덧셈 연산 결과 영상(출력) - 보통 설정하지 않음
# mask : 마스크 영상
# dtype : 출력 영상 타입 cv2.CV_8U(np.uint8)

# 밝기 조절 수식 : dst(x,y) = saturate(src(x,y) + n) 
# saturate: 0밑으로 내려가도 0, 255이상이어도 255
# 그래프에서 변동이 없는 구간 = saturate 연산 이루어지는 구간 

# 교재 p60 [표 4.1] numpy자료형, openCV자료형

import sys, cv2, numpy as np

## 흑백 영상 불러오기
# src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)
# if src is None:
#     print('Image load failed')
#     sys.exit()

# dst = src + 100 # numpy니까 100 그냥 더해주자(브로드캐스팅 연산 되니까) -> 가장 밝은 부분들이 검은색으로 바꼈다
# => 왜? 밝은 부분의 값은 거의 255에 가까웠을 텐데, 100을 더해서 255를 초과하니까 검은색이 됐다. 값을 초과했을 때는 255가 되도록 해주면 된다. 

# dst = cv2.add(src,100)
# dst = cv2.add(src,(100,0,0,0))
# 스칼라값 100을 넣은건데 내부적으로는 (100,0,0,0) 이렇게 들어간다(alpha까지)

## 컬러 영상 불러오기
src = cv2.imread('./images/lenna.bmp')
if src is None:
    print('Image load failed')
    sys.exit()

# dst = cv2.add(src,100) 
# dst = cv2.add(src,(100,0,0,0))
# 파란색 톤이 밝아졌다 -> rgb값이 들어오면서 'B'값만 100이 들어갔던 것.
dst = cv2.add(src,(100,100,100,0)) 
# 전체적으로 밝아진다.

# numpy 함수를 이용한 밝기 증가시키기
# dst = np.clip(src + 100. , 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()