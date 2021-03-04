import sys
import numpy as np
import cv2

def overlay(img, glasses, pos):
    # 실제 합성을 수행할 부분 영상 좌표 계산
    sx = pos[0]
    ex = pos[0] + glasses.shape[1]
    sy = pos[1]
    ey = pos[1] + glasses.shape[0]
    # sx, sy : start x,y좌표, ex, ey: end x,y좌표


    # 합성할 영역이 입력 영상 크기를 벗어나면 무시(합성 안함)
    if sx < 0 or sy < 0 or ex > img.shape[1] or ey > img.shape[0]:
        return

    img1 = img[sy:ey, sx:ex]   # shape=(h, w, 3) # 입력영상의 부분영상
    img2 = glasses[:, :, 0:3]  # shape=(h, w, 3) # 안경영상의 부분영상
    alpha = 1. - (glasses[:, :, 3] / 255.)  # shape=(h, w)
    # 가중치 왜? 
    # -> 안경 이미지의 털부분이 알파값을 보면 검은색 흰색 딱 나눠지는게 아니라 중간값이 있다.
    # 그 중간값을 합성하면 색이 하얗게 되거나 어색하게 되서 그 부분 좀 더 자연스럽게 하기 위해서 가중치를 줌.

    # BGR 채널별로 두 부분 영상의 가중합
    img1[..., 0] = (img1[..., 0] * alpha + img2[..., 0] * (1. - alpha)).astype(np.uint8) # blue
    img1[..., 1] = (img1[..., 1] * alpha + img2[..., 1] * (1. - alpha)).astype(np.uint8) # green
    img1[..., 2] = (img1[..., 2] * alpha + img2[..., 2] * (1. - alpha)).astype(np.uint8) # red 각각 가중치줘서 자연스럽게 하려고

# 영상 불러오기
cap = cv2.VideoCapture('./video/face_video.mp4')
if not cap.isOpened():
    print('Camera open failed!')
    sys.exit()

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('./video/output_f.avi', fourcc, 30, (w, h))

# Haar-like XML 파일 열기
face_classifier = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt2.xml')
eye_classifier = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

if face_classifier.empty() or eye_classifier.empty():
    print('XML load failed!')
    sys.exit()

# 안경 PNG 파일 열기 (Image from http://www.pngall.com/)
glasses = cv2.imread('./images/glasses.png', cv2.IMREAD_UNCHANGED)
if glasses is None:
    print('PNG image open failed!')
    sys.exit()

# 합성할 안경영상의 계산된 눈의 좌표 위치
ew, eh = glasses.shape[:2]  
ex1, ey1 = 240, 300
ex2, ey2 = 660, 300

# 프레임별 안경 합성
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 속도향상을 위해 파라미터 지정
    faces = face_classifier.detectMultiScale(frame, scaleFactor=1.2,
                                             minSize=(100, 100), maxSize=(800, 800))

    for (x, y, w, h) in faces:
        # 눈 검출
        faceROI = frame[y:y + h // 2, x:x + w] # 이마에서부터 눈까지만 자름
        eyes = eye_classifier.detectMultiScale(faceROI)

        if len(eyes) != 2: # 양쪽 눈이 안보이면 패쓰
            continue

        # x, y = 얼굴위치 좌표. 두 눈에 대한 중앙위치
        x1 = x + eyes[0][0] + (eyes[0][2] // 2) 
        y1 = y + eyes[0][1] + (eyes[0][3] // 2)
        x2 = x + eyes[1][0] + (eyes[1][2] // 2) 
        y2 = y + eyes[1][1] + (eyes[1][3] // 2)

        # eye1 = frame[y1-50:y1+50, x1-50:x1+50]
        # eye2 = frame[y2-50:y2+50, x2-50:x2+50] # 찍어보니까 왼쪽오른쪽 막 왔다갔다함(계속 뒤바뀜)
        # cv2.imshow('eye1',eye1)
        # cv2.imshow('eye2',eye2)

        # 눈의 위치가 바뀔 수 있기 때문에 스와핑(계속 뒤바뀜)
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1

        # 두 눈 사이의 거리에 대한 비율
        fx = (x2 - x1) / (ex2 - ex1)
        glasses2 = cv2.resize(glasses, (0, 0), fx=fx, fy=fx, interpolation=cv2.INTER_AREA) # 비율대로 안경 이미지 resize
        # interpolation=cv2.INTER_AREA : 이미지가 축소됐을 때 더 좋은 성능을 보이도록 설정한 부분

        # 크기 조절된 안경 영상을 합성할 위치 계산 (좌상단 좌표)
        pos = (x1 - int(ex1 * fx), y1 - int(ey1 * fx)) # resize했으니까 그 비율에 맞춰 좌표 다시 설정
        # pos = 안경을 그릴 시작 좌표

        # pos 위치에 합성을 해주는 함수
        overlay(frame, glasses2, pos)

    # 프레임 저장 및 화면 출력
    out.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()