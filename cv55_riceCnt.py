## 모폴로지 연산 함수
# cv2.morphologyEx(src, op, kernel, dst=None, anchor=None, iterations=None, borderType=None, borderValue=None)

# op: 모폴로지 연산 플래그 설정(cv2.MORPH_ERODE:침식, cv2.MORPH_DILATE:팽창
#                             cv2.MORPH_OPEN:열기, cv2.MORPH_CLOSE:닫기
#                             cv2.MORPH_GRADIENT:모폴로지 그래디언트 = 팽창-침식)

import cv2, sys, numpy as np

src = cv2.imread('./images/rice.png', cv2.IMREAD_GRAYSCALE)
if src is None:
    print("Image load failed")
    sys.exit()

# 지역 이진화 수행
dst1 = np.zeros(src.shape, np.uint8)

bw = src.shape[1] // 4
bh = src.shape[0] // 4

for y in range(4):
    for x in range(4):
        src_ = src[y*bh:(y+1)*bh, x*bw:(x+1)*bw]
        dst_ = dst1[y*bh:(y+1)*bh, x*bw:(x+1)*bw]

        # dst_를 파라미터로 사용하면 입력 및 출력으로 사용할 수 있다.
        cv2.threshold(src_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)

# 흰색 덩어리들을 계산해줌(정수값으로 리턴)
cnt1, _ = cv2.connectedComponents(dst1) # -> 그 객체(흰색)의 개수를 리턴해줌. + labels(이 리턴값은 뒤에서 다시 다룸)
print('cnt1 : ',cnt1) # 113 -> 잡음까지 모두 포함된 값. 정확히 개수를 파악하려면 잡음을 없애야 함.

# 열기 연산은 노이즈 제거
# dst2 = cv2.morphologyEx(dst1, cv2.MORPH_OPEN, None)

## 모폴로지를 쓰지 않고 노이즈 제거
dst2 = cv2.erode(dst1, None) # 침식연산(먼저)
dst2 = cv2.dilate(dst2, None) # 팽창연산(그다음). 침식 결과를 입력으로 넣어줌.

cnt2, _ = cv2.connectedComponents(dst2)
print('cnt2 : ',cnt2) # 99

cv2.imshow('src', src)
cv2.imshow('dst1', dst1) # 약간의 잡음이 남아있다. 이런거 제거할 때 쓰는 것.
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()

cv2.connectedComponentsWithStats()