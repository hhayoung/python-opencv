import sys
import cv2
import numpy as np

# 교재 p.55-56

# setMouseCallback(windowName, onMouse, param)
# windowName : 마우스 이벤트 처리를 수행할 창이름
# onMouse : 마우스 이벤트 처리를 위한 콜백함수 이름.(=이벤트핸들러) (콜백: 내가 호출하는게 아니라 시스템이 호출하는거)
# param : 콜백함수에 전달할 데이터

# onMouse(event, x, y, flags, param) : 이벤트 처리함수(이 함수의 이름은 얼마든지 바꿀 수 있다.)
# event : 마우스 이벤트 종류, cv2.EVENT_ 로 시작하는 상수
# x, y : 이벤트가 발생할 좌표
# flags : 마우스 이벤트가 발생했을 때의 상태
# param : setMouseCallback 일반적으로 적도록 되어있다.

# flags
# cv2.EVENT_FLAG_LBUTTON    : 1 (마우스 왼쪽 버튼이 눌렸을 때의 상태값)
# cv2.EVENT_FLAG_RBUTTON    : 2 (마우스 오른쪽 버튼이 눌렸을 때의 상태값)
# cv2.EVENT_FLAG_MBUTTON    : 4 (마우스 가운데 버튼(휠)이 눌렸을 때의 상태값)
# cv2.EVENT_FLAG_CTRLKEY    : 8 (CTRL 키가 눌렸을 때의 상태값)
# cv2.EVENT_FLAG_SHIFTKEY   : 16 (SHIFT 키가 눌렸을 때의 상태값)
# cv2.EVENT_FLAG_ALTKEY     : 32 (ALT 키가 눌렸을 때의 상태값)

# 이벤트들은 원래 윈도우가 가져가는데(이벤트 드리븐(event-driven)방식)
# opencv로 가져오려고 onMouse(이벤트핸들러)를 등록해서 그때부터 발생하는 이벤트는 opencv에서 처리하게 되는 것.

# pre_x = pre_y = -1  # -1로 하면 화면이 안보일 테니
def on_mouse(event, x, y, flags, param):

    global img
    global pre_x, pre_y

    # 마우스를 좌클릭했을 때
    if event == cv2.EVENT_LBUTTONDOWN:
        pre_x, pre_y = x, y
        print('EVENT_LBUTTONDOWN: {}, {}'.format(x,y))
    
    # 클릭하고 손을 뗐을 때
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: {}, {}'.format(x,y))

    # event를 체크할 때는 ==, flags 체크할 때는 & 연산자
    elif event == cv2.EVENT_MOUSEMOVE:
        # 그냥 마우스가 움직일 때마다 동작
        # print('EVENT_MOUSEMOVE: {}, {}'.format(x,y))
        # 왼쪽 버튼이 눌린 상태에서 움직일 때만 동작
        # if flags == cv2.EVENT_FLAG_LBUTTON:
        #     print('EVENT_MOUSEMOVE: {}, {}'.format(x,y))
              # 왼쪽버튼을 누른 상태로 shift나 ctrl을 같이 누르면 동작하지 않는다.
        if flags & cv2.EVENT_FLAG_LBUTTON:
            # print('EVENT_MOUSEMOVE: {}, {}'.format(x,y))
            # cv2.circle(img, (x,y), 5, (0,0,255), -1)
            # -> 빨리 그리면 속도를 못 따라옴. circle말고 line으로 처리하면 됨.

            # 직전의 점의 위치를 기억하고 있어야 한다. -> LBUTTON이 눌렸을 떄의 값 저장
            cv2.line(img, (pre_x, pre_y), (x,y), (0,130,255), 5, cv2.LINE_AA)
            cv2.imshow("image", img)
            pre_x, pre_y = x, y

img = np.ones((480,640,3), dtype=np.uint8) * 255  # -> 이렇게 해주면 흰색

cv2.namedWindow("image")
cv2.setMouseCallback("image", on_mouse)  # 콜백함수 등록. 이제부터 발생하는 이벤트는 opencv가 처리할 거야! 하고 알려주는 것.
# 이제부터 발생하는 이벤트는 on_mouse가 캐치해서 처리한다.

cv2.imshow('image',img)
cv2.waitKey()

cv2.destroyAllWindows()