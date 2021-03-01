import sys, cv2, numpy as np

# 트랙바를 2개 만들어서 상한값과 하한값 조정. -> 원하는 색 영역을 선택할 수 있도록

src = cv2.imread('./images/candies.png')
if src is None:
    print('Image load failed')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# 트랙바 이벤트 핸들러(트랙바 움직일 때마다 이벤트 발생(호출))
def onChange(pos):
    H_min = cv2.getTrackbarPos('H_min', 'dst')
    H_max = cv2.getTrackbarPos('H_max', 'dst')

    dst = cv2.inRange(src_hsv, (H_min,150,0),(H_max,255,255))
    cv2.imshow('dst', dst)

cv2.imshow('src',src)
cv2.namedWindow('dst')
# 트랙바 콜백 함수 등록
# cv2.createTrackbar('H_min', 'dst', 0, 179, onChange) # 초기값x
# cv2.createTrackbar('H_max', 'dst', 0, 179, onChange)
cv2.createTrackbar('H_min', 'dst', 50, 179, onChange) # 초기값o
cv2.createTrackbar('H_max', 'dst', 80, 179, onChange)
onChange(0) # 이 코드가 없으면 창이 뜨자마자는 결과가 보이지 않는다. 
# 뭔가 값을 넘겨줘야 이벤트가 발생하니까 기본값 0을 넘겨주는 것 같다. 
# 초기값을 정해놨기 때문에 여기에 0이 아닌 다른 값을 넣어도 50과 80이 선택된 결과가 출력된다.

cv2.waitKey()
cv2.destroyAllWindows()