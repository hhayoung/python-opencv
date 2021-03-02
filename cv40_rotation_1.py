import sys, cv2, math, numpy as np

src = cv2.imread('./images/img_1.png')
if src is None:
    print('Image load failed')
    sys.exit()

# degree를 radian 단위로 수정
# rad = 45 * math.pi / 180  # 반시계 방향
rad = -45 * math.pi / 180  # 시계 방향

aff = np.array([[math.cos(rad), math.sin(rad), 0],
                [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)

dst = cv2.warpAffine(src, aff, (0,0))

cv2.imshow('src',src)
cv2.imshow('dst',dst) # 원점중심으로 반시계방향으로 1radian 회전됨.
cv2.waitKey()

cv2.destroyAllWindows()