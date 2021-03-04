import sys
import numpy as np
import cv2


# 영상 불러오기()
src1 = cv2.imread('./images/graf1.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('./images/graf3.png', cv2.IMREAD_GRAYSCALE)

if src1 is None or src2 is None:
    print('Image load failed!')
    sys.exit()

# 특징점 알고리즘 객체 생성 (KAZE, AKAZE, ORB 등)
# feature = cv2.KAZE_create()
# feature = cv2.AKAZE_create() # KAZE에서 속도를 향상시킨 알고리즘
feature = cv2.ORB_create(1000) # 기본값 500

# 특징점 검출
kp1 = feature.detect(src1)  # return : keypoints
kp2 = feature.detect(src2)

# 특징점 개수
print('# of kp1:', len(kp1))
print('# of kp2:', len(kp2))

# 검출된 특징점 출력 영상 생성
dst1 = cv2.drawKeypoints(src1, kp1, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
dst2 = cv2.drawKeypoints(src2, kp2, None,
                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2) # 원안에 선이 그어져 있음 -> 방향. 디스크립터를 나타냄. 
# KAZE() - 벡터가 0도. 아직 계산을 안해줬기 때문에
# AKAZE() - 방향이 잡힘. 
# ORB() - 
cv2.waitKey()
cv2.destroyAllWindows()