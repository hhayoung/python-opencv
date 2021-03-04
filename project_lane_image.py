## RGB와 ROI를 이용해서 차선 검출하기

import sys, cv2, numpy as np

# ROI 영역
def region_of_interest(img, vertices, color3=(255,255,255), color1=255):
    mask = np.zeros_like(img)

    if len(img.shape) > 2: # 이미지 채널이 3개면
        color = color3
    else: # 흑백 이미지면
        color = color1
    
    # vertices에 정한 점들로 이뤄진 ROI 영역을 color로 채움
    cv2.fillPoly(mask, vertices, color)

    # img와 ROI영역 합침
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image

# 흰색 영역 찾기
def mark_img(img, blue_th = 200, green_th = 200, red_th=200):
    # BGR 제한값
    bgr_th = [blue_th, green_th, red_th]

    # BGR 제한 값보다 작으면 검은색으로
    thresholds = (src[:,:,0] < bgr_th[0]) |  (src[:,:,1] < bgr_th[1]) |  (src[:,:,2] < bgr_th[2])
    mark[thresholds] = [0,0,0] #검은색
    return mark


src = cv2.imread('./project/lane.jpg')
if src is None:
    print('Image load failed')
    sys.exit()

height, width = src.shape[:2] # 이미지 높이, 너비

# 사다리꼴 모형의 Points
vertices = np.array([[(50, height), (width/2-45, height/2+60), (width/2+45, height/2+60), (width-50, height)]], dtype=np.int32)
roi_img = region_of_interest(src, vertices) #vertices에 정한 점들 기준으로 ROI 생성

mark = np.copy(roi_img)
cv2.imshow('1', mark)
mark = mark_img(roi_img)
cv2.imshow('2', mark)

# cv2.imshow('src',src)
# cv2.imshow('white', mark)
cv2.waitKey()
cv2.destroyAllWindows()