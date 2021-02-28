# 프레임 :
# 동영상은 정지영상(정지이미지)이 여러 장이 모여서 동영상이 된다.
# 프레임/초 -> 1초동안 정지영상을 몇 장 보여줄건지
# 보통 영화는 초당 30프레임
# 예를 들어, 3초짜리 동영상의 프레임속도가 24.00/초라고 한다면 24프레임 * 3초 = 총 72개의 이미지를 보여주는 것.
# 동영상을 편집하려면, 필요한 부분을 짤라와서 수정한 뒤 다시 합쳐서 동영상을 만드는 것. (각각의 프레임을 수정하는 것)
# 코덱 : 인코딩된 것을 압축하는 프로그램(인코딩 -> 디코딩)

# Fourcc(4-문자코드, four character code)
# 동영상 파일의 코덱, 압축방식, 색상, 픽셀 등을 정의하는 정수값

# 4글자(Fourcc)
# *'DIVX' : DIVX MPEG-4 코덱,   <-일반적으로 많이 사용
# *'XVID' : XVID MPEG-4 코덱, 
# *'FMP4' : FFMPEG MPEG-4 코덱,  
# *'X264' : H.264/AVC 코덱,  
# *'MJPG' : Motion-JPEG-4 코덱

import sys
import cv2

# 비디오 파일 /카메라 열기: cv2.VideoCapture 클래스(카메라와 동영상 모두 가져올 수 있다)
cap = cv2.VideoCapture('./video/video_1.mp4') # 여기서 cap은 인스턴스

if not cap.isOpened():  # 비디오/카메라 isOpened() 둘 다 사용
    print('Video open failed')
    sys.exit()

# 교재 p25-26 [표 2.2]
# 교재 p26 [표 2.3]
# 비디오 프레임 크기, 전체 프레임 수, FPS(초당 프레임 수)
print('Frame Width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))  # get의 리턴값은 실수형 값 -> 필요에 따라 int형으로 형변환 해야할 떄도 있다.
print('Frame Height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('Frame Count:', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

fps = cap.get(cv2.CAP_PROP_FPS)
print('FPS:', cap.get(cv2.CAP_PROP_FPS))

# 비디오 각 프레임 처리
while True:
    ret, frame = cap.read() # 제대로 읽어오면 True반환

    if not ret: # 제대로 읽어오지 못했으면
        break

    # inversed = ~frame # 매 프레임마다 반전효과를 준 것.  
    # ~: 비트연산자. 주어져있는 rgb색상값의 값들을 비트연산한 것.

    edge = cv2.Canny(frame, 50, 150) # 매 프레임마다 윤곽선만 잡아낸 것.
    
    
    cv2.imshow('frame', frame)
    # cv2.imshow('inversed', inversed)
    cv2.imshow('edge', edge)


    if cv2.waitKey(20) == 27:  # ESC키 누르면
        break


cap.release()  # 불러온 걸 반환
cv2.destroyAllWindows()

