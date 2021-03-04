# 그랩컷 함수
# cv2.grabCut(img, mask, rect, bgdModel, fgdModel, iterCount, mode=None) -> mask, bgdModel, fgdModel
# img : 입력영상, 8비트 3채널
# mask : 입출력 마스크, cv2.GC_BGD(0), cv2.GC_FGD(1), cv2.GC_PR_BGD(2), cv2.GC_PR_FGD(3) 4개의 값으로 구성
#       GC-grabcut, BGD-background, FGD-foreground, PR-probably
#       확실히 배경일 때 = 0, 확실히 전경일 때 = 1, 배경같은거 = 2, 전경같은거 = 3
# rect : ROI 영역, cv2.GC_INIT_WITH_RECT모드에서만 사용
# bgdModel : 임시 배경 모델 행렬
# fgdModel : 임시 전경 모델 행렬
#       그랩컷을 했을 때 완벽하게 전경과 배경이 나뉘지 않음 -> 그럼 몇번의 그랩컷을 더 해야 하는데
#       기존에 변경된 값을 어디에 저장해놔야한다. 몇 번이나 그랩컷을 할 지 모르기 때문에 그 전의 결과를 저장해 두어야 함. 
#       그 전의 결과를 저장해놓는 변수로 bgdModel, fgdModel 를 사용하는 것.
# iterCount : 반복횟수
# mode : cv2.GC_INIT_WITH_RECT, cv2.GC_INIT_WITH_MASK 둘 중 하나 사용

import sys, cv2, numpy as np

src = cv2.imread('./images/zebra.jpg')
src = cv2.imread('./images/giraffe.jpg')
if src is None:
    print('Image load failed')
    sys.exit()

rc = cv2.selectROI(src)
mask = np.zeros(src.shape[:2], np.uint8)

cv2.grabCut(src, mask, rc, None, None, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==0) | (mask==2), 0, 1).astype('uint8')
# np.where(조건, 조건에 맞을 때 값, 조건과 다를 때 값)
# 확실한 백그라운드이거나 백그라운드 같은 거일 때는 0으로 하고 아니면 1
# 조건이 만족하면 0, 아니면 1 (여기서 0은 배경, 1은 전경)

dst = src * mask2[:,:,np.newaxis]
# np.newaxis는 axis를 하나 추가함. 차원이 늘어난다.
# mask2는 2차원이라서 3차원으로 만드는거(축 하나가 더 늘어난다)
# src는 컬러영상이라 3차원이니까 맞춰주는 거 같음
# mask2에는 0과1밖에 없기 때문에 곱하기니까 값이 1인 부분만 결과로 나온다.

# cv2.imshow('mask',mask)
# cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()

cv2.destroyAllWindows()