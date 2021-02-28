import sys
import cv2

cap = cv2.VideoCapture('./video/video_1.mp4')

if not cap.isOpened():
    print('Video open falied')
    sys.exit()

# int형변환도 되고, 반올림해도 되고
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
print(fourcc)

# 비디오 출력 : VideoWriter(filename, fourcc, fps, framesize, isColor(기본값True))
out = cv2.VideoWriter('./video/outVideo.avi', fourcc, fps, (w,h))

if not out.isOpened():
    print('File open failed')
    cap.release()
    sys.exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # inversed = ~frame
    # out.write(inversed)

    edge = cv2.Canny(frame, 50, 150)  # Canny의 리턴값은 grayScale 
    edge_2 = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR) # 컬러로 변환시켜줘야 한다.
    # out.write(edge) # 영상 재생을 할 수 없음
    out.write(edge_2)

    cv2.imshow('frame', frame)
    # cv2.imshow('inversed', inversed)
    cv2.imshow('edge', edge) # grayscale
    cv2.imshow('edge_2', edge_2) # truecolor -> 메모리 소비량이 더 많음.

    if cv2.waitKey(20) == 27:
        break


cap.release()
out.release()
cv2.destroyAllWindows()







