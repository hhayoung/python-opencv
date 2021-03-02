# 오츠알고리즘
import cv2, sys, numpy as np

src = cv2.imread('./images/rice.png', cv2.IMREAD_GRAYSCALE)
if src is None:
    print("Image load failed")
    sys.exit()

# 이때의 tresh값은 무조건 0, 리턴된 th값에는 오츠에 의해 결정된 임계치가 저장된다.
# 대표값 0을 주면 알아서 계산해줌, threshold값을 지정해도 otsu가 알아서 내부적으로 계산
# th, dst = cv2.threshold(src, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# th, dst = cv2.threshold(src, 50, 255, cv2.THRESH_OTSU) # or연산 생략 가능
th, dst = cv2.threshold(src, 50, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU) # 반대로 계산한 값

print("오츠의 임계치 : ", th)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()

cv2.destroyAllWindows()