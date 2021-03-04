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
    bgr_th = [blue_th, green_th, red_th] # 흰색
    # bgr_th = [83, 121, 156] # 노란색

    # BGR 제한 값보다 작으면 검은색으로
    thresholds = (img[:,:,0] < bgr_th[0]) |  (img[:,:,1] < bgr_th[1]) |  (img[:,:,2] < bgr_th[2])
    mark[thresholds] = [0,0,0] #검은색
    return mark


cap = cv2.VideoCapture('./project/road.mp4')
# cap = cv2.VideoCapture('./project/driving.mp4')
if not cap.isOpened():
    print('Video open failed')
    sys.exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)

    height, width = frame.shape[:2] # 이미지 높이, 너비

    # 사다리꼴 모형의 Points
    vertices = np.array([[(50, height), (width/2-45, height/2+40), (width/2+120, height/2+40), (width-50, height)]], dtype=np.int32)
    # vertices = np.array([[(50, height), (width/2-100, height/2+40), (width/2+50, height/2+40), (width-50, height)]], dtype=np.int32)
    roi_img = region_of_interest(frame, vertices) #vertices에 정한 점들 기준으로 ROI 생성

    mark = np.copy(roi_img)
    cv2.imshow('mark',mark)
    mark = mark_img(roi_img)

    # 흰색 차선 검출한 부분을 원본 frame에 overlap 하기
    color_th = (mark[:,:,0] == 0) & (mark[:,:,1] == 0) & (mark[:,:,2] == 0)
    frame[color_th] = [0,0,0]

    
    cv2.imshow('dst', frame)

    if cv2.waitKey(100) == 27:
        break

cap.release()
cv2.destroyAllWindows()
