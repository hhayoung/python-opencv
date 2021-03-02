# 동전 10,100원 구별
# 동전 검출하기 -> 허프 원 검출
# 동전 구분하기 -> 색상 정보 이용
import sys, cv2, numpy as np

# 입력 영상 불러오기
src = cv2.imread('./images/coin2.jpg')
if src is None:
    print('Image load failed')
    sys.exit()

# 히스토그램 그리는 함수
def getHistDraw(hist):
    imgHist = np.full((100,180), 255, dtype=np.uint8)
    histMax = np.max(hist)
    for x in range(180):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x,0] * 100 / histMax))
        cv2.line(imgHist, pt1, pt2, 0)
    return imgHist

# 허프변환 시 블러처리 하는게 성능이 좋음
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) # 원검출을 위해 그레이스케일로 변환
# 허프변환 함수가 노이즈에 민감하기 때문에 가우시안 블러로 노이즈 제거
blur = cv2.GaussianBlur(gray, (0,0), 1) # (src, ksize, sigmaX)

# 허프변환 원 검출 함수
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, param1=150, param2=35, minRadius=20, maxRadius=80) # 파라미터들 테스트 필요

# 원 검출 결과 및 동전 금액 출력
sum_of_money = 0
dst = src.copy()
if circles is not None:
    # print(circles.shape)
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
        # 10원 동전의 경우 빨간색 성분이 있어서 2개의 범위로 나뉘니까 그걸 shift로 땡겨오는 것.
        # shift를 안했을 경우 빨간색 성분은 히스토그램에서 양끝에 있을 텐데 그러면 판별하기가 힘들다.
        # 땡겨와서 연결되도록 해줘야 한다.
        # 조명때문에 붉은빛이 들어가는 경우가 있어서 전체적으로 shift를 통해 이동시키는 것.
        
        # 객체의 평균 색, 흑백 모드에서는 객체의 평균 강도
        # print(cv2.mean(hist_shift, mask)) # (55.56461475743987, 0.0, 0.0, 0.0)
        mean_of_hue = cv2.mean(hist_shift, mask)[0]  # mask 범위만 hue평균 계산하기
        # print(mean_of_hue)

        # 히스토그램 -> 색의 분포를 확인해보려고 hue를 넣는다.
        hist = cv2.calcHist([hue], [0], None, [256], [0, 180])
        hist_chart = getHistDraw(hist)
        # 10원과 100원의 분포도 차이가 크게 없다. 

        cv2.imshow('crop', crop)
        cv2.imshow('mask', mask)
        cv2.imshow('hist_chart', hist_chart)
        cv2.waitKey()
        cv2.destroyWindow('crop')
        cv2.destroyWindow('mask')
        cv2.destroyWindow('hist_chart')

        # Hue 평균이 59보다 작으면 10원, 59보다 크면 100원으로 간주
        # -> mean_of_hue 값을 출력해서 10원과 100원의 값을 알아냈다.
        won = 100
        if mean_of_hue < 59:
            won = 10
        sum_of_money += won
        
        cv2.putText(crop, str(won), (20,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,0,0), 2, cv2.LINE_AA)

# cv2.putText(img, text, org(출력시작좌표), fontFace, fontScale(폰트크기), color(폰트색상), thickness(폰트두께), lineType(선종류))
cv2.putText(dst, str(sum_of_money) + ' won', (40,80), cv2.FONT_HERSHEY_DUPLEX, 2, (255,0,0),2, cv2.LINE_AA)

cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()