import cv2
import numpy as np

# ROI(Region of Interest) : 관심영역
# : 영상에서 어떤 특정한 연산을 수행하고자 할 때 사용하는 임의의 부분 영역

# 마스크 영상: 물체의 본체를 따서 흰색으로 채운 이미지. 흰색은 불투명, 검은색은 투명으로 처리된다.
#           : 0과 1의 차이는 눈으로 확인하기 힘드므로 보통 마스크 영상으로는 0 또는 255로 구성된 이진 영상 사용

# 마스크 연산을 하기 위한 함수
# cv2.copyTo(src, mask, dst)
# src : 입력 영상
# mask : 마스크 영상 : 0이 아닌 값(픽셀)에 대해서만 연산(복사)을 수행. (0은 검은색이니까 흰색부분만 복사)
# dst : 출력 영상
# 3개의 이미지 사이즈가 전부 동일해야 한다. src와 dst 영상 타입이 같아야 한다.(grayscale-grayscale, truecolor-truecolor)

# src = cv2.imread('./images/airplane.bmp', cv2.IMREAD_COLOR)
# mask = cv2.imread('./images/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
# dst = cv2.imread('./images/field.bmp', cv2.IMREAD_COLOR)

# # src와 dst는 타입이 같아야 함(grayscale, turecolor)
# # cv2.copyTo(src, mask, dst) # 첫번째 방법

# # numpy의 boolean 인덱싱을 이용하여 처리해보기
# # dst영상에 src의 마스크 영역을 할당해보세요.
# dst[mask > 0] = src[mask > 0] # 두번째 방법

# cv2.imshow('src', src)
# cv2.imshow('mask', mask)
# cv2.imshow('dst', dst)

# cv2.waitKey()

# cv2.destroyAllWindows()


## 알파채널을 마스크 영상으로 활용하여 영상을 합성하기

# 보통 이미지는 rgb차원을 가지고 잇는데, png는 알파(투명도)라는 차원이 하나 더 올라감.
# 투명한 이미지 같은 경우 4차원
# jpg는 3차원, png는 4차원

# 투명도가 있는 이미지를 다른 이미지 위에 올리기

src = cv2.imread('./dog_img.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('./images/opencv-logo-white.png', cv2.IMREAD_UNCHANGED) # 이미지가 알파 채널을 가지고 있는 경우

# 4개의 채널 B,G,R,A(alpha)
# b = logo[:,:,0]
# g = logo[:,:,1]
# r = logo[:,:,2]
# alpha = logo[:,:,3]
mask = logo[:,:,3] # mask는 알파 채널로 만드는 역할을 하는 영상
# cv2.imshow('mask', mask)

# 마지막 mask 를 슬라이싱 한 나머지 b, g, r을 가져옴(4차원에서 나머지 BGR 3차원을 가져온 것)
logo = logo[:,:,:-1] # logo[:,:,3]을 제외한 나머지 채널
# cv2.imshow('logo', logo)
# cv2.waitKey()

h, w = mask.shape[:2] # 마스크의 가로, 세로 값
# crop = src[0:h, 0:w] # 로고 위치를 옮기려면 값을 주면 된다. 

# crop은 src의 부분영역을 참조하고 있음.(즉, crop은 src의 부분영역임)
crop = src[200:200+h, 200:200+w] # -> copy()함수를 사용하지 않아서 참조하고 있는 것.
crop = src[200:200+h, 200:200+w].copy() # 이렇게 복사하고 logo를 붙이면, 원본(src)에는 영향을 주지 않는다.

cv2.copyTo(logo, mask, crop) # BGR logo를 mask에 의해서 crop에다가 적용한 것. crop크기는 src의 크기
# crop[mask > 0] = logo[mask > 0]

cv2.imshow('src',src) # 그래서 src를 출력해도 crop이 출력되는 것과 같다. 
cv2.imshow('crop',crop) 
cv2.imshow('logo',logo)
cv2.imshow('mask',mask)
cv2.waitKey()

cv2.destroyAllWindows()