import cv2, sys, numpy as np

src = cv2.imread('./images/rose.png', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('Image load failed')
    sys.exit()

blur = cv2.GaussianBlur(src, (0,0), 2)
# dst = src - blur  # 이렇게는 안됨
# dst = cv2.subtract(src, blur)

# 가중치를 주고 결과에 128을 더해줌으로써 눈으로 식별할 수 있도록 함.
# dst = cv2.addWeighted(src, 1, blur, -1, 128) # src는 1, blur는 -1로 가중치를 줌.

dst = np.clip(2.0*src - blur, 0, 255).astype(np.uint8) # 훨씬 선명해짐. 모두 다 계산하고나서 uint8로 변환

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()