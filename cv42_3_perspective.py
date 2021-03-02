## 마우스 이벤트로 좌표값 가져오기

import sys, cv2, numpy as np

src = cv2.imread('./images/name_card_3.jpg')
if src is None:
    print('Image load failed')
    sys.exit()

x_pt = []
y_pt = []
def on_mouse(event, x, y, flags, param):
    # 마우스를 좌클릭했을 때
    if event == cv2.EVENT_LBUTTONDOWN:
        print('좌표: {}, {}'.format(x,y))
        x_pt.append(x)
        y_pt.append(y)
        # print('x_pt = ',x_pt)
        # print('y_pt = ',y_pt)

cv2.namedWindow("src")
cv2.setMouseCallback("src", on_mouse)
cv2.imshow('src',src)
key = cv2.waitKey()
if key==ord(' '):
    cv2.destroyWindow('src')

# 일반 명함카드 비율 (9:5)
w, h = 720, 400

# 소스의 좌표
src_Coord = np.array([[x_pt[0], y_pt[0]],[x_pt[1], y_pt[1]],[x_pt[2], y_pt[2]],[x_pt[3], y_pt[3]]], dtype=np.float32)
# 출력 좌표
dst_Coord = np.array([[0,0],[w-1,0],[w-1,h-1],[0,h-1]], dtype=np.float32)
# 투시변환행렬
per_matrix = cv2.getPerspectiveTransform(src_Coord, dst_Coord)

per_dst = cv2.warpPerspective(src, per_matrix, (w,h))

##### 샤프닝 : 글씨 더 선명하게 해주기 
# YCrCb로 변환
dst_ycrcb = cv2.cvtColor(per_dst, cv2.COLOR_BGR2YCrCb)
# 채널 분리
channels = cv2.split(dst_ycrcb)
# Y채널만 블러처리
channels[0] = cv2.GaussianBlur(channels[0], (0,0), 2)
# 다시 합쳐줌
dst_ycrcb_blur = cv2.merge(channels)
dst_blur = cv2.cvtColor(dst_ycrcb_blur, cv2.COLOR_YCrCb2BGR)
dst = np.clip(2.0*per_dst - dst_blur, 0, 255).astype(np.uint8) # 훨씬 선명해짐


cv2.imshow('dst',dst)
cv2.waitKey()

cv2.destroyAllWindows()