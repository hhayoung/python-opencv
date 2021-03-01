import sys, cv2, numpy as np

############## 히스토그램 그리는 함수 ##############
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
###################################################

# CrCb의 살색 히스토그램을 얻어오기

reference_img = cv2.imread('./images/son2.png')
mask = cv2.imread('./images/son2_mask.bmp', cv2.IMREAD_GRAYSCALE)

ref_ycrcb = cv2.cvtColor(reference_img, cv2.COLOR_BGR2YCrCb)

######## 채널별 분리 ########
ycrcb_channels = cv2.split(ref_ycrcb)
############################

channels = [1,2] # cr,cb채널
ranges = [0, 256, 0, 256]
# cr,cb채널의 히스토그램 => 2차원 히스토그램
hist = cv2.calcHist([ref_ycrcb], channels, mask, [128,128], ranges)
# -> 가로축, 세로축이 cr, cb로 되어있고
# cr, cb 히스토그램이 중앙에 분포되어있는 것처럼 2차원 히스토그램도 중앙쪽에 위치하고 있다.

###### cr, cb 채널 각각 히스토그램 구하기 => 1차원 히스토그램 ######
hist_cr = cv2.calcHist([ycrcb_channels[1]], [0], None, [256], [0, 256])
cr_hist_chart = getHistDraw(hist_cr)
hist_cb = cv2.calcHist([ycrcb_channels[2]], [0], None, [256], [0, 256])
cb_hist_chart = getHistDraw(hist_cb)
################################################################

hist_norm = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U) # 손흥민꺼 히스토그램

## 기성용 이미지에 적용하기
src = cv2.imread('./images/ki.png')
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

backproj = cv2.calcBackProject([src_ycrcb],channels, hist, ranges, 1) # 손흥민꺼 적용해서 역투영
# cv2.imwrite('./images/k1_mask.bmp', backproj)

cv2.imshow('src',src)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('backproj',backproj)

###### cr, cb 히스토그램 출력 #######
cv2.imshow('cr_hist_chart',cr_hist_chart)
cv2.imshow('cb_hist_chart',cb_hist_chart)
####################################

# 손흥민이나 기성용이나 축구선수고 비슷하게 타고 그래서 완벽히 얼굴부분이 잡힌거같은데
# 아이유 사진으로 해보니까 희미하게 잡힘. 아예 피부 히스토그램이 다르다는 소리 

cv2.waitKey()
cv2.destroyAllWindows()

