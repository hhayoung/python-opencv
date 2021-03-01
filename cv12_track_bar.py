# 교재 p.56 트랙바
import numpy as np
import cv2

# 트랙바(Trackbar)
# cv2.createTrackbar(trackbarName, windowName, value, count, onChange) : 트랙바 생성 함수
# trackbarName : 트랙바 이름
# windowName : 트랙바를 생성할 창이름
# value : 트랙바의 위치 초기값
# count : 트랙바 최대값
# onChange : 트랙바의 위치가 변경될 떄마다 호출되는 콜백 함수 이름
# : onChange(pos) position

def on_level_changed(pos):
    print(pos)

    level = pos * 16    # 최대값16 * 16 = 256
    
    # if level >= 255:
    #     level = 255
    level = np.clip(level, 0, 255) # 0보다 작은 값은 0, 255보다 큰 값은 255

    img[:,:] = level    # grayscale이니까 밝기가 바뀔 것.
    cv2.imshow('image', img)

img = np.zeros((480,640), np.uint8)

# cv2.namedWindow('image') # 창코드를 따로 만드는 경우 이 다음 코드에 트랙바 생성.
# cv2.createTrackbar

cv2.imshow('image', img)
# 창 만드는 코드가 따로 없는 경우 imshow() 다음에 트랙바 생성
cv2.createTrackbar('level', 'image', 0, 16, on_level_changed)
cv2.waitKey()

cv2.destroyAllWindows()


### 교재 예제문제

# def onChange(pos):
#     global img

#     r = cv2.getTrackbarPos('R', 'image')
#     g = cv2.getTrackbarPos('G', 'image')
#     b = cv2.getTrackbarPos('B', 'image')

#     img[:] = (b,g,r)
#     cv2.imshow('image', img)

# img = np.zeros((512,512,3), np.uint8)
# cv2.imshow('image', img)

# # 트랙바 생성
# cv2.createTrackbar('R', 'image', 0, 255, onChange)
# cv2.createTrackbar('G', 'image', 0, 255, onChange)
# cv2.createTrackbar('B', 'image', 0 255, onChange)

# # 트랙바의 위치 초기화
# cv2.setTrackbarPos('R', 'image', 0)
# cv2.setTrackbarPos('G', 'image', 0)
# cv2.setTrackbarPos('B', 'image', 255)

# cv2.waitKey()
# cv2.destroyAllWindows()