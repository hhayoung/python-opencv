import sys
import numpy as np
import cv2

# 키보드 이벤트
# cv2.waitKey(delay) => retVal
# delay: 밀리초단위 대기시간. delay <= 0 : 무한정 대기, 기본값은 0
# retVal: 눌린 키 값(ASCII code). 키가 눌리지 않으면 -1
# 참고 : waitKey() 함수는 OpenCV 창이 하나라도 있을 때 동작함.
# : 특정 키 입력을 확인하려면 ord() 함수를 이용
# 주요 특수키 : ESC(27), ENTER(13), TAB(9)

img = cv2.imread('./dami.jpg', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed')
    sys.exit()

cv2.namedWindow('image')

cv2.imshow('image', img)

# 'i' 또는 'I' 키가 눌렸을 때 반전효과가 적용된 이미지를 출력하도록 하세요. (단, ESC 키가 눌렸을 때는 종료되도록 하세요.)
while True:
    keycode = cv2.waitKey()

    if keycode == ord('i') or keycode == ord('I'):
        img = ~img
        cv2.imshow('image', img)
    elif keycode == 27:
        break

cv2.destroyAllWindows()