import cv2
import numpy as np
from tkinter import *
# OpenCV와 tkinter를 결합해 GUI로 표시할 때 PIL 라이브러리 활용
from PIL import Image # pip install pillow
from PIL import ImageTk
from tkinter import filedialog

file_name = './images/soccer_01.jpg'
title_name = 'Haar cascade 얼굴 검출'
frame_width = 500

def selectFile():
    file_name =  filedialog.askopenfilename(initialdir = "./images/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print('File name : ', file_name) # 이미지 경로 리턴됨.
    read_image = cv2.imread(file_name)
    (height, width) = read_image.shape[:2]
    frameSize = int(sizeSpin.get())
    ratio = frameSize / width
    dimension = (frameSize, int(height * ratio)) # spinbox에 있는 가로값에 맞춰 세로 길이 정하기
    
    read_image = cv2.resize(read_image, dimension, interpolation = cv2.INTER_AREA)

    # tkinter의 색상 체계는 openCV와 다르게 RGB 패턴을 사용하므로 BGR -> RGB
    image = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image) # Numpy 배열을 Image 객체로 변환
    imgtk = ImageTk.PhotoImage(image=image) # tkinter와 호환되는 객체로 변환
    detectAndDisplay(read_image)
    
def detectAndDisplay(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray) # 좀 더 선명하게 하기 위한 평활화

    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray) # 얼굴 검출
    for (x,y,w,h) in faces:
        
        center = (x + w//2, y + h//2)
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 4)
        faceROI = frame_gray[y:y+h,x:x+w]

        #-- In each face, detect eyes
        eyes = eyes_cascade.detectMultiScale(faceROI) # 눈 검출
        for (x2,y2,w2,h2) in eyes:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round((w2 + h2)*0.25))
            frame = cv2.circle(frame, eye_center, radius, (255, 0, 0), 4)

    # cv2.imshow('Capture - Face detection', frame)
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image) # Image객체로 변환

    # 객체로 변환하기
    imgtk = ImageTk.PhotoImage(image=image) # tkinter와 호환되는 객체로 변환

    detection.config(image=imgtk) # 이미지 갱신을 위해 config를 통해 image 매개변수 설정
    detection.image = imgtk # garbage collector가 이미지를 삭제하지 않도록 한 번 더 등록
    
#main
main = Tk()
main.title(title_name)
main.geometry()

read_image = cv2.imread("./images/soccer_01.jpg")
(height, width) = read_image.shape[:2]
ratio = frame_width / width
dimension = (frame_width, int(height * ratio)) # frame_width에 맞춰 세로길이 맞춰짐(기존이미지의 비율대로)
read_image = cv2.resize(read_image, dimension, interpolation = cv2.INTER_AREA)
# interpolation=cv2.INTER_AREA : 이미지가 축소됐을 때 더 좋은 성능을 보이도록 설정한 부분

image = cv2.cvtColor(read_image, cv2.COLOR_BGR2RGB) # tkinter 의 색상 체계는 RGB
image = Image.fromarray(image) # numpy배열에서 Image 객체로 변환
imgtk = ImageTk.PhotoImage(image=image) # tkinter에 호환되는 객체로 변환시키고 그걸 뿌려줘야함.

face_cascade = cv2.CascadeClassifier()
eyes_cascade = cv2.CascadeClassifier()

#-- 1. Load the cascades
if not face_cascade.load('./haarcascades/haarcascade_frontalface_alt2.xml'):
    print('--(!)Error loading face cascade')
    exit(0)
if not eyes_cascade.load('./haarcascades/haarcascade_eye.xml'):
    print('--(!)Error loading eyes cascade')
    exit(0)

label=Label(main, text=title_name)
label.config(font=("Courier", 18)) # 폰트지정
label.grid(row=0,column=0,columnspan=4)
sizeLabel=Label(main, text='Frame Width : ')                
sizeLabel.grid(row=1,column=0)
sizeVal  = IntVar(value=frame_width)

sizeSpin = Spinbox(main, textvariable=sizeVal,from_=0, to=2000, increment=100, justify=RIGHT) # 0~2000까지 100단위씩
sizeSpin.grid(row=1, column=1)
Button(main,text="File Select", height=2,command=lambda:selectFile()).grid(row=1, column=2, columnspan=2, sticky=(W, E))

detection=Label(main, image=imgtk) # label의 image매개변수를 이용하면 이미지를 표시할 수 있다.
detection.grid(row=2,column=0,columnspan=4)
detectAndDisplay(read_image)

main.mainloop()