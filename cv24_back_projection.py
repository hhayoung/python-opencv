# 색상을 추출하는 방법 -> 특정 컬러를 지정해서 그 컬러값을 얻어오는 방법 
# -> 또다른 방법. 특정 컬러로 지정할 수 없느 컬러들이 있기 떄문에 
# 역으로 우리가 컬러를 지정해서 지정된 컬러를 해당 사진으로부터 갖는게 아니라
# 우리가 촬영한 거에서 범위를 지정해서 그 컬러값을 지정해서 
# 그 사진에 해당되는 컬러를 끄집어 오는거 
# 원색계열의 컬러를 찍어왔다면, 반대로 
# 교재 p.115

# 해당 사진에서 해당 히스토그램을 뽑아와서 , 다른 사진에서 히스토그램 그거랑 비슷한거를 다른 사진에서 컬러값 뽑아오기
# 실제 사진과 동영상에서 히스토그램을 추출한 샘플을 가지고,
# 그 샘플을 가지고 다른 사진과 동영상에서 컬러를 추출한다.

# 히스토그램 역투영(back projection)
# 히스토그램 역투영 함수
# : calcBackProject(images, channels, hist, ranges, scale, dst)

# 영역을 선택할 수 있도록 하는 함수 
# cv2.selectROI(src) -> 선택하기 위한 창이 뜬다.

import sys, cv2, numpy as np

src = cv2.imread('./images/grass_land.png')
if src is None:
    print('Image load failed')
    sys.exit()

# ROI selector 창 생성(영역을 선택할 수 있는 창 생성)
x,y,w,h = cv2.selectROI(src) # 창이 뜬다. 추출하고자 하는 범위를 지정해준다. 리턴 값 -> 그 영역의 좌표, 너비, 높이

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
# 해당 좌표에서 우리가 지정한 범위만 잘라 올 것
crop_zone = src_ycrcb[y:y+h, x:x+w]

channels = [1,2] # ycrcb에서 y는 밝기니까 빼고 분석하려는 건 cr,cb 두 채널
histSize = [128, 128] # 막대 사이즈
cr_range = [0,256]
cb_range = [0,256]
ranges = cr_range + cb_range
hist = cv2.calcHist([crop_zone], channels, None, histSize, ranges)

# 선택 영역을 정규화한거
hist_norm = cv2.normalize(hist, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 입력 영상 전체에 대한 히스토그램 역투영
backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1) # 구해오기. hist_norm을 통해서
dst = cv2.copyTo(src, backproj) # 그런 뒤 마스크연산
# 마스크연산을 하게 된다. hist_norm랑 일치하는 것만 가져와서 copyTo를 이용해 마스크연산함.

cv2.imshow('backproj', backproj)

cv2.imshow('hist_norm', hist_norm) # 초원의 히스토그램, 히스토그램 2차원으로 출력된 것
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()