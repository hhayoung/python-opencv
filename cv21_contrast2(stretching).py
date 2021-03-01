## 스트레칭

import sys, cv2, numpy as np

# 히스토그램 그리는 함수
def getHistDraw(hist):
    imgHist = np.full((100,256), 255, dtype=np.uint8)
    print(hist.shape)
    print(np.max(hist))
    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x,0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)
    return imgHist

src = cv2.imread('./images/equal_test.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed')
    sys.exit()

# 정규화 함수 : cv2.normalize(src, dst, alpha, beta, norm_type, dtype, mask)
# norm_type(정규화 타입) : 최소,최대값으로 
# dst는 어짜피 리턴받을거니까 보통 None으로 사용

dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX) # 범위를 0~255로 scale한다고 봐도 된다.

# 히스토그램 구하기
hist = cv2.calcHist([src], [0], None, [256], [0, 256])
src_hist_chart = getHistDraw(hist)
hist = cv2.calcHist([dst], [0], None, [256], [0, 256])
dst_hist_chart = getHistDraw(hist)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
# 히스토그램 출력
cv2.imshow('src_hist_chart',src_hist_chart)
cv2.imshow('dst_hist_chart',dst_hist_chart)

cv2.waitKey()
cv2.destroyAllWindows()