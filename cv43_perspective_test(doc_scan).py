# 코드분석

## 이미지에서 직접 자를 영역을 드래그로 지정해서 투시변환하기

import sys, cv2, numpy as np

# 선택영역 지정할 도형
def drawROI(img, corners):
    cpy = img.copy() # 전송받은 이미지의 복사본 만들기
    c1 = (192,192,255) # 컬러설정
    c2 = (128,128,255) # 컬러설정

    for pt in corners:
        # c1컬러로 원을 그린다.
        cv2.circle(cpy, tuple(pt), 25, c1, -1, cv2.LINE_AA)
        # pt는 현재 리스트형태라서 tuple로 형변환
    
    # 각 코너는 튜플로 변환
    cv2.line(cpy, tuple(corners[0]), tuple(corners[1]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[1]), tuple(corners[2]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[2]), tuple(corners[3]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[3]), tuple(corners[0]), c2, 2, cv2.LINE_AA)

    # 가중치 합성
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)

    return disp

# 마우스이벤트 핸들러
def onMouse(event, x, y, flags, param):
    global src_Coord, dragSrc, ptOld, src

    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(4):
            # 원안의 좌표를 클릭하면(사각형꼭지점에서부터의 거리)
            if cv2.norm(src_Coord[i] - (x,y)) < 25: # cv2.norm()은 거리계산하는 함수, 25는 서클의 반지름
                dragSrc[i] = True # 클릭된 원만 True값으로
                ptOld = (x,y) # 클릭했을 때의 상태좌표값 저장(이전좌표로 쓰일 변수)
                break
    if event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i] = False
    if event == cv2.EVENT_MOUSEMOVE:
        for i in range(4):
            if dragSrc[i]: # 클릭된 원만 이동
                # 이전 좌표값을 알고 있어야 한다.
                dx = x - ptOld[0] # 변이값(현재 좌표 - 이전좌표)
                dy = y - ptOld[1] # 변이값(현재 좌표 - 이전좌표)

                src_Coord[i] += (dx, dy) # 움직인 만큼만 원래 값에 +-

                # 이동한 좌표로 다시 화면에 뿌려줘야함
                cpy = drawROI(src, src_Coord)
                cv2.imshow('img', cpy)
                ptOld = (x,y) # 마우스가 움직일때마다 이벤트가 일어나는 것이기 때문에 계속 상태좌표를 저장해둬야한다.
                break

src = cv2.imread('./images/a4_paper.jpg')
if src is None:
    print('Image load failed')
    sys.exit()

h, w = src.shape[:2]
dw = 500

# A4 용지 크기 : 210x297cm, 세로 크기 설정
dh = round(dw * 297/210) # 설정한 dw값에 a4비율이 되도록 a4비율로 나눠줘서 세로 크기 얻어내기
src_Coord = np.array([[30,30],[30,h-30],[w-30,h-30],[w-30,30]], np.float32)

# 출력영상의 좌표(반시계 방향)
dst_Coord = np.array([[0,0],[0,dh-1],[dw-1, dh-1],[dw-1,0]], np.float32)
dragSrc = [False, False, False, False]

# 모서리점, 사각형 그리기
disp = drawROI(src, src_Coord)

cv2.imshow('img', disp)
cv2.setMouseCallback('img', onMouse)

while True:
    key = cv2.waitKey()
    if key == 13: # 엔터누르면 빠져나오기
        break
    elif key == 27: # ESC누르면 강제종료
        cv2.destroyWindow('img')
        sys.exit()

# 투시변환
pers = cv2.getPerspectiveTransform(src_Coord, dst_Coord)
dst = cv2.warpPerspective(src, pers, (dw, dh), flags=cv2.INTER_CUBIC)

# 결과 영상 출력
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()