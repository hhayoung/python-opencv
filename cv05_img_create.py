import numpy as np
import cv2

## 영상 생성하기
# numpy를 이용해서 직접 창 만들기
# img1 = np.empty((240, 320), dtype=np.uint8) # 사이즈(세로, 가로):2차원  # grayscale
# img2 = np.zeros((240, 320, 3), dtype=np.uint8) # color image
# img3 = np.ones((240, 320), dtype=np.uint8) # grayscale
# img4 = np.full((240, 320, 3), (0,255,0), dtype=np.uint8) # 이 때의 색상은 BGR 순서

# 헷갈렸던 부분 : color image의 dtype도 np.uint8인 것.
# -> ppt에 있는 걸로 헷갈려하면 안되고, uint8로 하는 것이 가장 안전한 방법이라고 알려져 있다.
# uint32인 것도 uint8로 하기도 함. 
# 2차원, 3차원 이미지들(+영상데이터)이 보통 다 dtype은 uint8이다. 

# cv2.imshow('img1', img1) # 초기화되지 않은 쓰레기값이 들어가있음.
# cv2.imshow('img2', img2) # 검은색
# cv2.imshow('img3', img3) # 1이나 0이나 별 차이없어서 검은색으로 보임
# cv2.imshow('img4', img4) # 지정한 색으로 출력

# cv2.waitKey()

# cv2.destroyAllWindows()

## 복사하기
# img1 = cv2.imread('./images/cat_test.jpg')

# img2 = img1 # 참조 이미지

# # 새로 만들어서 처리해야 하는 경우
# img3 = img1.copy() # 메모리에 새로 할당한 복사본

# # img1[:,:] = (0, 255, 0)
# img2[10:20,10:20] = 0  # img1에도 영향을 끼친다.(제대로 복사가 되지 않고 참조하는 상태)
# img3[10:20,10:20] = (0,0,255)  # img1에 영향을 끼치지 X(제대로 복사가 되서 독립된 상태)

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2) # img2가 img1을 참조하고 있다. 복사가 된 게 x
# cv2.imshow('img3', img3) # 복사됨.
# cv2.waitKey()

# cv2.destroyAllWindows()


## 부분적 영상 추출
# img1 = cv2.imread('./dami.jpg')

# # 슬라이싱이 가능한 이유 : 데이터가 numpy이기 때문에
# img2 = img1[40:120, 30:150] # numpy.ndarray의 슬라이싱
# img3 = img1[40:120, 30:150].copy()

# img1[:,:] = (0,255,255)
# img2.fill(0)  # 잘라온 영상의 값을 채웠을 때 참조본에도 값이 채워진다. 

# # 원그리기
# cv2.circle(img2, (20, 20), 10, (0, 0, 255), 2) # 중심점위치(가로,세로), 반지름 10, 컬러(B,G,R), 선두께 2

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)

# cv2.waitKey()
# cv2.destroyAllWindows()