import numpy as np
import cv2


img = np.full((600, 450, 3), (255,255,255), dtype=np.uint8)

# cv2.rectangle(img, pt1, pt2, color, thickness, lineType, shift)
# cv2.circle(img, center, radius, color, thickness, lineType, shift)
# cv2.ellipse(img, center, size(가로세로사이즈), 앵글, 시작각도, 끝각도, color, thickness, lineType, shift)
# cv2.polylines(img, pts, isClose(다각형이 열렸냐 닫혔냐 boolean값), color, thickness, lineType, shift)
# pts = np.array([[300,200],[300,150],[350,300],[250,300]]) # 2차원 배열로 좌표값 설정
# cv2.polylines(img, [pts], True, (180,180,180), 5) # 마지막 좌표값과 첫번째 좌표값을 이어줌.

# 비모 몸통
cv2.rectangle(img, (0,0),(550,750), (157,186,47), -1) # (70,220): 사각형의 왼쪽 위의 좌표, (180,280): 오른쪽 아래 좌표. thickness = -1 : 색상 채우기

# 비모 얼굴
cv2.rectangle(img, (70,70),(380,300), (175,213,161), -1) 
# 비모 얼굴 테두리
cv2.rectangle(img, (70,70),(380,300), (0,0,0), 5, lineType=cv2.LINE_AA)

# 비모 눈
cv2.ellipse(img, (150,150), (8,10), 0, 0, 360, 0, -1, lineType=cv2.LINE_AA)
cv2.ellipse(img, (300,150), (8,10), 0, 0, 360, 0, -1, lineType=cv2.LINE_AA)

# 비모 입
cv2.ellipse(img, (225,160), (25,13), 0, 0, 180, 0, 5, lineType=cv2.LINE_AA) # 180도하니까 반만 그려진다.

# 비모 몸통
# 초록색 버튼
cv2.rectangle(img, (80,350),(215,378), (23,45,17), -1)
cv2.rectangle(img, (80,350),(215,378), 0, 5, lineType=cv2.LINE_AA)

# 보라색 버튼
cv2.circle(img, (345,360), 17, (109,44,36), -1, lineType=cv2.LINE_AA)
cv2.circle(img, (345,360), 17, 0, 5, lineType=cv2.LINE_AA)

cv2.rectangle(img, (80,500),(145,520), (109,44,36), -1)
cv2.rectangle(img, (80,500),(145,520), 0, 5)
cv2.rectangle(img, (160,500),(225,520), (109,44,36), -1)
cv2.rectangle(img, (160,500),(225,520), 0, 5)

# 노랑색 버튼
pts = np.array([[80,430],[105,430],[105,405],[130,405],[130,430],[155,430],[155,455],[130,455],[130,480],[105,480],[105,455],[80,455]])
cv2.fillPoly(img, [pts], (7,214,252))
cv2.polylines(img, [pts], True, 0, 5, lineType=cv2.LINE_AA)

# 하늘색 버튼
pts = np.array([[300,385],[278,430],[322,430]])
cv2.fillPoly(img, [pts], (244,200,53))
cv2.polylines(img, [pts], True, 0, 5, lineType=cv2.LINE_AA)

# 연두색 버튼
cv2.circle(img, (370,450), 16, (67,194,125), -1, lineType=cv2.LINE_AA)
cv2.circle(img, (370,450), 16, 0, 5, lineType=cv2.LINE_AA)

# 빨간색 버튼
cv2.circle(img, (315,495), 32, (36,30,237), -1, lineType=cv2.LINE_AA)
cv2.circle(img, (315,495), 32, 0, 5, lineType=cv2.LINE_AA)

cv2.imshow('img',img)
cv2.waitKey()

cv2.destroyAllWindows()