# 고양이 영상 스페이스바로 필터 전환하기
import sys, cv2, numpy as np

cap = cv2.VideoCapture('./video/dami.mp4')
if not cap.isOpened():
    print('Video open failed')
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
print(fourcc)

out = cv2.VideoWriter('./video/outDami3.mp4',fourcc, fps, (w,h))

if not out.isOpened():
    print('File open failed')
    cap.release()
    sys.exit()

# 만화필터
def filter_1(img):
    h, w = img.shape[:2]
    small_img = cv2.resize(img, (w//2, h//2))

    blur = cv2.bilateralFilter(small_img, -1, 20, 8)
    edge = 255-cv2.Canny(small_img, 80, 130)  # Canny()를 적용하면 그레이스케일로 변한다.
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR) # 다시 BGR로 변경
    dst = cv2.bitwise_and(blur, edge)

    # dst = cv2.resize(dst, (w,h)) # 원래 사이즈로 변환
    dst = cv2.resize(dst, (w,h), interpolation=cv2.INTER_NEAREST) # 보간법이용. 더 거친 영상

    return dst

# 스케치필터
def filter_2(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (0,0), 3)
    dst = cv2.divide(gray, blur, scale=255)
    dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

    return dst

delay = round(1000/fps)
mode = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    elif mode == 1:
        frame = filter_1(frame)
    elif mode == 2:
        frame = filter_2(frame)

    cv2.imshow('frame', frame)
    out.write(frame)
    
    key = cv2.waitKey(delay)

    if key == ord(' '):
        mode += 1
        if mode == 3:
            mode = 0
    elif key == 27: #ESC
        break


out.release()
cap.release()
cv2.destroyAllWindows()