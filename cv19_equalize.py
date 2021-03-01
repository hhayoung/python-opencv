## 평활화

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

## 그레이스케일 영상의 히스토그램 평활화
src = cv2.imread('./images/equal_test.jpg', cv2.IMREAD_GRAYSCALE)

dst = cv2.equalizeHist(src)

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


## 컬러 영상 히스토그램의 평활화
# src = cv2.imread('./images/equal_test.jpg')
# rgb 각각 분리해서 각각 평활화(한번에는 ㄴㄴ) 그 뒤에 각각 평활화한 것을 모아줌.
# YCrCb를 이용. Y(밝기)만 바꾸면 된다.

# rgb로 평활화 하지 않는 이유
# -> rgb를 각각 평활화 시켜버리면, 색상 성분이 변해버림.
# 다시 merge해서 합쳤을 때 원래 색이 안나오고 변할 수가 있다.

# YCrCb로 사용하면 Y(밝기)만 평활화 시키기 때문에 색상 성분의 변형이 일어날 일이 없다.
# 원색상은 유지하면서 명암비만 선명하게 할 수 있다. 

## ------------- YCrCb로 변환하기 -------------
# src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb) # YCrCb 로 변환
# channels = cv2.split(src_ycrcb) # Y, Cr, Cb 분리

# 밝기 성분에 대해서만 히스토그램 평활화 하기
# channels[0] = cv2.equalizeHist(channels[0]) # Y채널만 평활화

# dst_ycrcb = cv2.merge(channels) # Y, Cr, Cb 병합. YCrCb상태
# dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR) # BRG 상태

## ------------- BGR로 평활화하기 -------------
# src = cv2.imread('./images/equal_test.jpg')
# channels = cv2.split(src)

# for i in range(3):
#     channels[i] = cv2.equalizeHist(channels[i])
# dst = cv2.merge(channels)


# cv2.imshow('src',src)
# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()