import sys, cv2, numpy as np

src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed')
    sys.exit()

# 명암비를 조절하는 수식
# dst(x,y) = saturate(1+alpha)*src - 128*alpha

# alpha = 0.5 # 기울기
alpha = 2.0  # alpha값 클수록 명암이 진해진다.
dst = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8)
# np.clip(array, min, max) : array값들에 대해서 min보다 작은 값들은 min, max보다 큰 값들은 max로 바꿔주는 함수
# --> alpha 값을 변경해주면서 원하는 명암비를 설정할 수 있다.

cv2.imshow('src',src)
cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()