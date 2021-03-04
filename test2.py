
# import sys, cv2, numpy as np

# src = cv2.imread('./images/test_coin.jpg')
# if src is None:
#     print('Image load failed')
#     sys.exit()

# # 허프변환 함수가 노이즈에 민감하기 때문에 가우시안 블러로 노이즈 제거
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (0,0), 1) # (src, ksize, sigmaX)

# # 허프변환 원 검출 함수
# circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, param1=77, param2=46, minRadius=28, maxRadius=120) # 파라미터들 테스트 필요

# # 원 검출 결과 및 동전 금액 출력
# sum_of_money = 0
# dst = src.copy()
# if circles is not None:
#     for i in range(circles.shape[1]): # 동전 갯수만큼 shape=(1,N,3)
#         cx, cy, radius = circles[0][i] # 앞에 0은 무조건 넣어줌
#         cv2.circle(dst, (cx,cy), radius, (255,0,255), 2, cv2.LINE_AA)

#         # 동전 영역 부분 영상 추출
#         x1 = int(cx - radius)
#         y1 = int(cy - radius)
#         x2 = int(cx + radius)
#         y2 = int(cy + radius)
#         radius = int(radius)

#         crop = dst [y1:y2, x1:x2, :]
#         ch, cw = crop.shape[:2]

#         # 동전 영역에 대한 ROI 마스크 영상 생성
#         mask = np.zeros((ch,cw), np.uint8)
#         cv2.circle(mask, (cw//2, ch//2), radius, 255, -1)

#         # *** hue 계산 
#         hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
#         hue, _, _ = cv2.split(hsv)
#         hist_shift = (hue + 50) % 180    # H의 범위는 0~179

#         # 객체의 평균 색, 흑백 모드에서는 객체의 평균 강도
#         mean_of_hue = cv2.mean(hist_shift, mask)[0]  # mask 범위만 hue평균 계산하기

#         cv2.imshow('crop', crop)
#         cv2.imshow('mask', mask)
#         cv2.waitKey()
#         cv2.destroyWindow('crop')
#         cv2.destroyWindow('mask')
#         cv2.destroyWindow('hist_chart')

#         won = 100
#         if mean_of_hue < 55:
#             won = 10
#         elif mean_of_hue > 120:
#             if radius >= 44:
#                 won = 500
#             elif radius >= 39:
#                 won = 100
#             elif radius >= 35:
#                 won = 50
#         sum_of_money += won
        
#         cv2.putText(crop, str(won), (20,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,0,0), 2, cv2.LINE_AA)

# cv2.putText(dst, str(sum_of_money) + ' won', (40,80), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0),2, cv2.LINE_AA)

# cv2.imshow('dst',dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

import sys, cv2, numpy as np

# 입력 영상 불러오기
src = cv2.imread('./images/test_coin2.jpg')
if src is None:
    print('Image load failed')
    sys.exit()

# 허프변환 시 블러처리 하는게 성능이 좋음
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) # 원검출을 위해 그레이스케일로 변환
# 허프변환 함수가 노이즈에 민감하기 때문에 가우시안 블러로 노이즈 제거
blur = cv2.GaussianBlur(gray, (0,0), 1) # (src, ksize, sigmaX)

# 허프변환 원 검출 함수
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, 
                        param1=120, param2=40, minRadius=22, maxRadius=93)

# 원 검출 결과 및 동전 금액 출력
sum_of_money = 0
dst = src.copy()
if circles is not None:
    for i in range(circles.shape[1]): # 동전 갯수만큼 shape=(1,N,3)
        cx, cy, radius = circles[0][i] # 앞에 0은 무조건 넣어줌
        cv2.circle(dst, (cx,cy), radius, (255,0,255), 2, cv2.LINE_AA)

        # 동전 영역 부분 영상 추출
        x1 = int(cx - radius)
        y1 = int(cy - radius)
        x2 = int(cx + radius)
        y2 = int(cy + radius)
        radius = int(radius)

        crop = dst [y1:y2, x1:x2, :]

        ch, cw = crop.shape[:2]

        # 동전 영역에 대한 ROI 마스크 영상 생성
        mask = np.zeros((ch,cw), np.uint8)
        cv2.circle(mask, (cw//2, ch//2), radius, 255, -1)

        # *** hue 계산 
        hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
        hue, _, _ = cv2.split(hsv)
        # print(hue)
        hist_shift = (hue + 50) % 180    # H의 범위는 0~179

        # 객체의 평균 색, 흑백 모드에서는 객체의 평균 강도
        mean_of_hue = cv2.mean(hist_shift, mask)[0]  # mask 범위만 hue평균 계산하기
        print(mean_of_hue)
        print(radius)
        print('-------')

        cv2.imshow('crop', crop)
        cv2.imshow('mask', mask)
        cv2.waitKey()
        cv2.destroyWindow('crop')
        cv2.destroyWindow('mask')
        cv2.destroyWindow('hist_chart')

        won = 100
        if mean_of_hue < 70:
            won = 10
        elif mean_of_hue > 90:
            if radius >= 48:
                won = 500
            elif radius >= 44:
                won = 100
            elif radius >= 40:
                won = 50
            elif radius < 40:
                won = 0
        sum_of_money += won
        
        cv2.putText(crop, str(won), (20,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,0,0), 2, cv2.LINE_AA)

cv2.putText(dst, str(sum_of_money) + ' won', (40,80), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0),2, cv2.LINE_AA)

cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()

