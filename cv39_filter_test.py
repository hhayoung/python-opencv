# 영상에 필터 효과 넣기
import sys, cv2, numpy as np

cap = cv2.VideoCapture('./video/eagle.avi')
if not cap.isOpened():
    print('Video open failed')
    sys.exit()

# 만화같은 필터
def filter_1(img):
    # blur = cv2.bilateralFilter(img, -1, 20, 8)
    # edge = 255-cv2.Canny(img, 80, 130)  # Canny()를 적용하면 그레이스케일로 변한다.
    # edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR) # 다시 BGR로 변경
    # 속도가 너무 느림 
    # -> 사이즈를 줄여서 처리하고 사이즈를 다시 키우기

    h, w = img.shape[:2]
    small_img = cv2.resize(img, (w//2, h//2))

    blur = cv2.bilateralFilter(small_img, -1, 20, 8)
    edge = 255-cv2.Canny(small_img, 80, 130)  # Canny()를 적용하면 그레이스케일로 변한다.
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR) # 다시 BGR로 변경

    dst = cv2.bitwise_and(blur, edge) # and연산. 
    #밝은부분 255 어두운부분 0, 각각의 값들을 비트연산
    # 엣지부분을 끄집어오기 위한 부분

    # dst = cv2.resize(dst, (w,h)) # 원래 사이즈로 변환
    dst = cv2.resize(dst, (w,h), interpolation=cv2.INTER_NEAREST) # 보간법이용. 더 거친 영상

    return dst

# 스케치 필터
def filter_2(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 가우시안 표준편차 3
    blur = cv2.GaussianBlur(gray, (0,0), 3) # (0,0) 자동으로 설정

    # gray를 blur로 나눠주고 255를 곱해줌.
    dst = cv2.divide(gray, blur, scale=255)
    '''
    gray가 변화가 큰 선, blur는 부드러운 곡선(그래프를 생각)
    나눠줬을 때의 마이너스값과 플러스값이 나오는데
    같은 부분은 1, gray가 blur보다 큰 부분은 1.xxx, gray가 blur보다 작은 부분은 0.xxx 
    여기에다가 255를 곱해주면 흰색(1 or 1.xxx) 또는 검은색(0.xxx)만 남게 된다. 
    엣지 부분만 검은색이 남는 것.
    '''
    
    return dst


while True:
    ret, frame = cap.read()
    if not ret:
        break

    # frame = filter_1(frame)
    frame = filter_2(frame)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27: #ESC
        break

cap.release()
cv2.destroyAllWindows()