# import cv2,sys, numpy as np

# src = cv2.imread('./dog_img.bmp')
# if src is None:
#     print('Image load failed')
#     sys.exit()

# cpy = src.copy()
# print(cpy.shape)
# rc1 = (530,140,90,80)
# rc2 = (700,120,110,80)

# cv2.rectangle(cpy, rc1, (0,0,255), 2)
# cv2.rectangle(cpy, rc2, (0,0,255), 2)
# cv2.imshow('src',cpy)
# cv2.waitKey()

# cv2.destroyAllWindows()

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# # 기성용 역투영 문제
# import cv2,sys, numpy as np

# ############## 히스토그램 그리는 함수 ##############
# def getHistDraw(hist):
#     imgHist = np.full((100,256), 255, dtype=np.uint8)
#     print(hist.shape)
#     print(np.max(hist))
#     histMax = np.max(hist)
#     for x in range(256):
#         pt1 = (x, 100)
#         pt2 = (x, 100 - int(hist[x,0] * 100 / histMax))
#         cv2.line(imgHist, pt1, pt2, 0)
#     return imgHist
# ###################################################

# ref = cv2.imread('./images/k1.png', cv2.IMREAD_COLOR)
# mask = cv2.imread('./images/k1_mask.bmp', cv2.IMREAD_GRAYSCALE)
# ref_ycrcb = cv2.cvtColor(ref, cv2.COLOR_BGR2YCrCb)

# ############ 채널별 분리 ############
# ycrcb_channels = cv2.split(ref_ycrcb)
# #####################################
# channels = [1, 2]
# ranges = [0, 256, 0, 256]
# hist = cv2.calcHist([ref_ycrcb], channels, mask, [128, 128], ranges)

# ############ cr, cb 채널 히스토그램 구하기 ############
# cr_hist = cv2.calcHist([ycrcb_channels[1]], [0], None, [256], [0,256])
# cb_hist = cv2.calcHist([ycrcb_channels[2]], [0], None, [256], [0,256])
# cr_hist_chart = getHistDraw(cr_hist)
# cb_hist_chart = getHistDraw(cb_hist)
# #####################################################

# # 역투영 적용 이미지
# src = cv2.imread('./images/k2.png', cv2.IMREAD_COLOR)
# src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
# backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)
# h, w = src.shape[:2]
# dst = np.zeros((h, w, 3), np.uint8)
# dst[backproj > 30] = src[backproj > 30]

# cv2.imshow('ref', ref)
# cv2.imshow('mask', mask)
# cv2.imshow('src', src)
# cv2.imshow('backproj', backproj)
# cv2.imshow('dst', dst)

# ###### cr, cb 히스토그램 출력 #######
# cv2.imshow('cr_hist_chart',cr_hist_chart)
# cv2.imshow('cb_hist_chart',cb_hist_chart)
# ####################################

# cv2.waitKey()
# cv2.destroyAllWindows()

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# # 로봇이랑 텍스트 합치기 문제

# import cv2, sys

# # 투명도가 있는 이미지를 다른 이미지 위에 올리기
# src = cv2.imread('./images/bg2.jpg', cv2.IMREAD_COLOR)
# logo = cv2.imread('./images/cv_txt.png', cv2.IMREAD_UNCHANGED)

# mask = logo[:,:,3] # 마스크영상
# edge = cv2.Canny(mask, 100,150) # 에지영상

# logo = logo[:,:,:-1] # logo[:,:,3]을 제외한 나머지 채널

# h, w = mask.shape[:2]

# # 복사본
# copy = src.copy()

# crop1 = src[400:400+h, 200:200+w]
# crop2 = copy[400:400+h, 200:200+w]

# cv2.copyTo(logo, mask, crop1)
# cv2.copyTo(logo, edge, crop2)

# # 참조하고 있기 때문에 crop, crop2를 찍지 않아도 된다.
# cv2.imshow('src',src)
# cv2.imshow('src2',copy)
# cv2.waitKey()

# cv2.destroyAllWindows()

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ


import sys, cv2, numpy as np

# src = cv2.imread('./images/old_tel.png')
# src = cv2.imread('./images/test_coin.jpg')
src = cv2.imread('./images/test_coin2.jpg')
if src is None:
    print('Image load failed')
    sys.exit()

# 블러처리 해서 노이즈 제거하면 성능이 좋아짐.
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (0,0), 1.0)

def on_trackbar(pos):
    # 트랙바에서 값 가져오기
    rmin = cv2.getTrackbarPos('minRadius', 'img')
    rmax = cv2.getTrackbarPos('maxRadius', 'img')
    th = cv2.getTrackbarPos('threshold', 'img')
    prm1 = cv2.getTrackbarPos('param1', 'img')

    # 원검출
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, 
                            param1=prm1, param2=th, minRadius=rmin, maxRadius=rmax)

    dst = src.copy()
    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = circles[0][i]
            cv2.circle(dst, (cx,cy), radius, (0,0,255), 2, cv2.LINE_AA)

    cv2.imshow('img', dst)


# 트랙바 생성
cv2.imshow('img',src)
cv2.createTrackbar('minRadius', 'img', 0, 100, on_trackbar)
cv2.createTrackbar('maxRadius', 'img', 0, 150, on_trackbar)
cv2.createTrackbar('threshold', 'img', 0, 100, on_trackbar)
cv2.createTrackbar('param1', 'img', 0, 255, on_trackbar)
cv2.setTrackbarPos('minRadius', 'img', 10)
cv2.setTrackbarPos('maxRadius', 'img', 80)
cv2.setTrackbarPos('threshold', 'img', 40)
cv2.setTrackbarPos('param1', 'img', 125)
cv2.waitKey()

cv2.destroyAllWindows()

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

