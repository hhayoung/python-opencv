# 영상의 속성

import cv2

# img1은 numpy.ndarray 타입이다.
# openCV는 영상 데이터를 표현할 때 numpy.ndarray로 표현한다. 
img1 = cv2.imread('./dami.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('./dami.jpg', cv2.IMREAD_COLOR)

print(type(img1)) # <class 'numpy.ndarray'>
print(type(img2)) # <class 'numpy.ndarray'>
print(img1.dtype) # uint8
print(img2.dtype) # uint8
print(img1.shape) # (960, 540)
print(img2.shape) # (960, 540, 3)

if len(img1.shape) == 2:
    print("img1은 그레이스케일")
elif len(img1.shape) == 3:
    print("img1은 트루컬러")

# img2의 이미지 사이즈 출력하기
# (960, 540, 3) -> 가로세로뒤바껴있다. 가로=540, 세로=960
h, w = img2.shape[:2]
print('img2 사이즈 : {} x {}'.format(w,h))

h, w = img1.shape
print('img1 사이즈 : {} x {}'.format(w,h))

## 영상의 픽셀값 참조하는 방법
x = 20
y = 10
p1 = img1[y,x]
print(p1) # 해당 픽셀에 해당되는 값

# img2의 해당 픽셀값 찍기
x = 20
y = 10
p2 = img2[y,x]
print(p2) # [ 41  85 126] -> 순서대로 BGR

# 영상에 값을 넣어보기
img1[y,x] = 0
img2[y,x] = (0,0,255)

# 전체 픽셀값을 해당 색상으로 바꾸고 싶을 때 
'''
for y in range(h):
    for x in range(w):
        img1[y,x] = 255
        img2[y,x] = (0,255,255)
'''
# 일일이 반복해서 넣는것보다 이 방식이 낫다. 
img1[:,:] = 255
img2[:,:] = (0,0,255)

cv2.imshow('img2',img2)
cv2.imshow('img1',img1)

cv2.waitKey()

cv2.destroyAllWindows()
