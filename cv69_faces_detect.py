import cv2
import numpy as np

def detectAndDisplay(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray) # 평활화 -> 좀 더 정확하게 찾기 위해서 선명하게

    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
        # 전체 영역이 아니라 각 얼굴영역에서 눈 찾도록

        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI)

        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv2.circle(frame, eye_center, radius, (255, 0, 0 ), 4)
        cv2.imshow('Capture - Face detection', frame)

img = cv2.imread("./images/soccer_01.jpg")

(height, width) = img.shape[:2]

cv2.imshow("Original Image", img)

face_cascade = cv2.CascadeClassifier()
eyes_cascade = cv2.CascadeClassifier()

#-- 1. Load the cascades
if not face_cascade.load('./haarcascades/haarcascade_frontalface_alt2.xml'):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load('./haarcascades/haarcascade_eye.xml'):
    print('--(!)Error loading eyes cascade')
    exit(0)

detectAndDisplay(img)

cv2.waitKey(0)
cv2.destroyAllWindows()