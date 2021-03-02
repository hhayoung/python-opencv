# 컬러이미지
import cv2, sys, numpy as np

src = cv2.imread('./images/rose.png')
if src is None:
    print('Image load failed')
    sys.exit()

## 내코드 ------------------------------------------
# YCrCb로 변환
# src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
# 채널 분리
# channels = cv2.split(src_ycrcb)
# Y채널만 블러처리
# channels[0] = cv2.GaussianBlur(channels[0], (0,0), 2)
# 다시 합쳐줌
# src_ycrcb_blur = cv2.merge(channels)
# src_blur = cv2.cvtColor(src_ycrcb_blur, cv2.COLOR_YCrCb2BGR)
# dst = np.clip(2.0*src - src_blur, 0, 255).astype(np.uint8) # 훨씬 선명해짐
## ------------------------------------------------

## 교수님 ------------------------------------------
# YCrCb로 변환
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
# split을 이용하지 않고 y채널 가져오기
# float32로 conversion을 하는 이유 : 중간과정에서 미세한 계산치가 사라지지 않도록 하기 위함
# 내부 연산을 한 후에 최종 결과를 확인할 때 uint8로 형변환 하는 것이 좋다. 
src_y = src_ycrcb[:,:,0].astype(np.float32)
# Y채널만 블러처리
blur = cv2.GaussianBlur(src_y, (0,0), 2.0)
# 계산하고 난 뒤 uint8로 변환
src_ycrcb[:,:,0] = np.clip(2.0*src_y - blur, 0, 255).astype(np.uint8)
dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)
## ------------------------------------------------

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()