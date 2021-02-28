import numpy as np
import cv2

# 각자의 도형을 그리는 함수가 있음. 함수마다 약간의 옵션이 다름.

### 직선 그리기
# cv2.line(img, pt1, pt2, color, thickness, lineType, shift, ...)
# img : 그릴 영상(캔버스, 도화지)
# pt1, pt2 : 선의 시작점, 끝점(튜플)
# color : 색상, thickness: 선의 두께(기본값 1)
# lineType : 선타입(cv2.LINE_4, cv2.LINE_8(기본값), cv2.LINE_AA(주로 많이 씀. 안티앨리어싱))
# 영상의 기본 단위는 픽셀. 곡선을 표현할 때, 픽셀로 표현되기 때문에 선을 확대시켜보면 계단모양으로 되어있을 것.(->앨리어싱)
# 계단모양을 없애주는 방법이 안티앨리어싱
# shift : 기본값 0, 좌표 값의 축소비율

# 검은색 바탕의 도화지를 만들고 싶으면 np.zeros()나 np.ones() 사용
# 흰색 바탕의 도화지 만들기
img = np.full((800, 800, 3), (255,255,255), dtype=np.uint8) # (행 800, 열 800) == (행이800개니까 세로, 열이800개니까 가로)
# img = np.full((800, 800, 3), 255, dtype=np.uint8) # 다 같은 값이면 한번만 적어도 된다.
# dtype=np.uint8 <- 영상 원소의 타입(각 픽셀 데이터타입). 다른걸 써도 되지만 uint8이 가장 안정적이다.

# 파란색 직선
cv2.line(img, (100,100), (300,100), (255,0,0), 5)
# 빨간색 대각선
cv2.line(img, (100,100), (300,300), (0,0,255), 10)


### 사각형 그리기 (2가지 방법)
# cv2.rectangle(img, pt1, pt2, color, thickness, lineType, shift)
# cv2.rectangle(img, rec, color, thickness, lineType, shift)

# 초록색보다 어두운 색으로 채우기된 사각형 그리기
cv2.rectangle(img, (70,220),(180,280), (0,128,0), -1) # (70,220): 사각형의 왼쪽 위의 좌표, (180,280): 오른쪽 아래 좌표. thickness = -1 : 색상 채우기
# 초록색 사각형 그리기
cv2.rectangle(img, (50,200,150,150), (0,255,0), 10) # (x,y,w,h): 왼쪽에서 50떨어지고, 위에서 200떨어지고, 150x150 사이즈 사각형 그리기


### 원 그리기
# cv2.circle(img, center, radius, color, thickness, lineType, shift)

cv2.circle(img, (300,300), 100, (255,255,0), 10) # 앨리어싱
cv2.circle(img, (500,300), 100, (255,0,255), -1, cv2.LINE_AA) # 안티앨리어싱


### 타원 그리기
# cv2.ellipse(img, center, size(가로세로사이즈), 앵글, 시작각도, 끝각도, color, thickness, lineType, shift)

# cv2.ellipse(img, (400,500), (200,150), 0, 0, 180, (0,0,255), 5) # 180도하니까 반만 그려진다.
# cv2.ellipse(img, (400,500), (200,150), 0, 0, 360, (0,0,255), 5) # 360도를 해야 원
cv2.ellipse(img, (400,500), (200,150), 90, 0, 360, (0,0,255), 5) 
cv2.ellipse(img, (400,500), (200,150), 45, 0, 360, (255,0,0), 5)  
cv2.ellipse(img, (400,500), (200,150), 0, 0, 360, (0,255,0), 5) # angle은 회전이라고 생각하면 됨. 


### 다각형 그리기
# cv2.polylines(img, pts, isClose(다각형이 열렸냐 닫혔냐 boolean값), color, thickness, lineType, shift)
pts = np.array([[300,200],[300,150],[350,300],[250,300]]) # 2차원 배열로 좌표값 설정

cv2.polylines(img, [pts], True, (180,180,180), 5) # 마지막 좌표값과 첫번째 좌표값을 이어줌.
pts = np.array([[400,200],[400,150],[450,300],[350,300]]) 
cv2.polylines(img, [pts], False, (180,180,180), 5) # 마지막 좌표값과 첫번째 좌표값을 잇지 않음.


### 문자열 출력
# cv2.putText(img, text, org(출력시작좌표), fontFace, fontScale(폰트크기), color(폰트색상), thickness(폰트두께), lineType(선종류), bottomLeftOrigin(기본값 False))

text = "My Picture"
cv2.putText(img, text, (200,600), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2) # 앨리어싱
cv2.putText(img, text, (200,600), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2, cv2.LINE_AA) # 안티앨리어싱 (글자는 안티앨리어싱 해주는게 좋다.)


cv2.imshow('img',img)
cv2.waitKey()

cv2.destroyAllWindows()