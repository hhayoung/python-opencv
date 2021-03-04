# 명함을 투시변환 한 후 명함의 텍스트 가져오기

# Tesseract
# 광학 문자 인식(OCR) 라이브러리
# 독일 만하임 대학교 사이트(https://github.com/UB-Mannheim/tesseract/wiki)
# : 텍스트 이미지를 문자열로 변환해줌

import sys
import random
import numpy as np
import cv2
import pytesseract

# 시작지점부터 반시계방향으로 맞추기 위한 함수
def reorderPts(pts):
    # 칼럼0 -> 칼럼1 순으로 정렬한 인덱스를 반환
    idx = np.lexsort((pts[:, 1], pts[:, 0]))
    print(pts[:,0]) # x축(width)
    print(pts[:,-1]) # y축(height)
    '''
    >a=[1,5,1,4,3,3]
    >b=[9,4,0,4,2,1]
    >idx = np.lexsort((b,a))
    >print(idx)
    => [ 2 0 5 4 3 1 ]
    ? a를 먼저 정렬해서 b에다가 적용
    a가 정렬이 되면 1 1 3 3 4 5 이 순서대로 b의 인덱스를 가져옴
    a> 1 5 1 4 3 3 
    b> 9 4 0 4 2 1
    a의 1에 해당되는 부분 b에서는 9와 0. 9보다 0이 더 빠르니까 0의 인덱스값 2가 넘어옴
    b의 인덱스를 얻어오는 방식
    '''
    print('인덱스 : ', idx)
    
    # x좌표 순으로 정렬
    pts = pts[idx]

    # print(pts) # x값(width)이 작은 순서대로
    '''
    [[226. 322.]
     [320. 112.]
     [713. 416.]
     [755. 174.]]
    '''
    # print(pts[0,1], pts[1,1]) # 322.0 112.0
    # print(pts[[0,1]], pts[[1,0]])   [[226. 322.] 
    #                                  [320. 112.]]
    #                                 [[320. 112.] 
    #                                  [226. 322.]]
    # print(pts[2,1], pts[3,1]) # 416.0 174.0
    # print(pts[[2,3]], pts[[3,2]])   [[713. 416.] 
    #                                  [755. 174.]]
    #                                 [[755. 174.] 
    #                                  [713. 416.]]

    ## 반시계 방향으로 정렬된 좌표 pts 구하기
    # x좌표 기준으로 y좌표값을 비교해서 
    # 1,2번째 꼭지점 중 y좌표가 더 큰 게 2번째로 갈 수 있도록 바꿔줌
    if pts[0, 1] > pts[1, 1]:
        pts[[0, 1]] = pts[[1, 0]]
        '''
        pts에다가 idx리스트를 넣어준 것. (x,y좌표 아님)
        [0,1]을 넣어주면 pts[0]과 pts[1]의 값을 가져오고,
        [1,0]을 넣어주면 pts[1]과 pts[0]의 값을 가져오므로
        둘이 한번에 바꿔줄 수 있다.
        '''
    # 3,4번째 꼭지점 중 y좌표가 더 큰 게 3번째로 갈 수 있도록 바꿔줌 -> 반시계방향으로 해야하니까
    if pts[2, 1] < pts[3, 1]:
        pts[[2, 3]] = pts[[3, 2]]

    # 반시계 방향으로 정렬된 좌표 리턴
    return pts 

# 영상 불러오기
# filename = './images/nc_1.jpg'
filename = './images/nc_2.jpg'
# filename = './images/nc_3.jpg'

# print(sys.argv) #['c:\\study\\comVision\\cv60_aaa.py']

# 명령인자를 넣어서 실행시키는 경우 -> 프롬프트창에서 사용
if len(sys.argv) > 1:
    filename = sys.argv[1]

src = cv2.imread(filename)

if src is None:
    print('Image load failed!')
    sys.exit()

# 가로 세로 지정(일반 명함카드 비율 (9:5))
dw, dh = 720, 400

srcCoord = np.array([[0, 0], [0, 0], [0, 0], [0, 0]], np.float32)
dstCoord = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32) # 시작점에서 반시계방향

dst = np.zeros((dh, dw), np.uint8)

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) # 그레이스케일영상으로 변환
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # 이진화
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # 명함의 외곽선 검출

cpy = src.copy()
for pts in contours: # 외곽선 검출된 개수만큼
    if cv2.contourArea(pts) < 1000: # 작은거 무시
        continue

    # 근사화
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)
    if not cv2.isContourConvex(approx) or len(approx) != 4: # 다각형이 아니거나 꼭지점이 4개가 아니면 무시
        continue

    # approx에는 각 꼭지점의 좌표 정보가 들어있다.
    cv2.polylines(cpy, [approx], True, (0, 255, 0), 2, cv2.LINE_AA)
    srcCoord = reorderPts(approx.reshape(4, 2).astype(np.float32)) # 모서리값은 순서가 정해져있지 않다. 반시계방향으로 맞춰줘야함.
    # srcCoord = approx.reshape(4, 2).astype(np.float32) # 그래서 이렇게 하면 안되는 것. 이번엔 운좋게 방향 맞았던 거
    # print(approx) # 원래는 3차원
    # print(approx.reshape(4, 2)) # 2차원으로


# 투시변환을 이용행서 영상 펴기
pers = cv2.getPerspectiveTransform(srcCoord, dstCoord)
dst = cv2.warpPerspective(src, pers, (dw, dh))

# tesseract 는 컬러영상에서도 괜찮지만, 보통 그레이스케일로 작업한다. 
dst_gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
print(pytesseract.image_to_string(dst_gray, lang='Hangul+eng'))


cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()