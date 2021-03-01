# 화면 전환할 때, 첫번째 영상(원숭이)의 끝부분과 두번째 영상(코끼리)의 시작부분을 합성해줘야 한다 .
# 전체 영상길이가 만약 5초랑 5초라고 하면 원숭이 뒷부분 2초와 코끼리 앞부분 2초를 합성시키려고 한다면
# 원숭이 마지막 2초 구간 또는 코끼리의 시작 2초 구간을 어떻게 따올까? 
# => 초당 프레임 개수를 가져와서 *초 를 해주면 된다.
# 슬라이드 전환이라고 한다면 코끼리가 나오면서 원숭이가 밀려나야 함.
# 코끼리 시작 2초 부분에서 슬라이싱해서 잘라오고, 원숭이 마지막 2초 부분에서도 슬라이싱해서 잘라와서 
# 두 잘라온 걸 합성영역에 합쳐서 표현해주면 된다. (numpy라서 슬라이싱)
# 원숭이 구간이 처음에는 더 많았다가 점점 원숭이 슬라이싱영역이 작아지고, 코끼리 슬라이싱영역이 커지면 됨.

import sys
import numpy as np
import cv2

# 두개의 동영상 불러오기
cap1 = cv2.VideoCapture('./video/video_1.mp4')
cap2 = cv2.VideoCapture('./video/video_2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed')
    sys.exit()

# 첫번째 동영상의 전체 프레임 개수
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
# 두번째 동영상의 전체 프레임 개수
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = round(cap1.get(cv2.CAP_PROP_FPS)) # 둘 다 24프레임이라서 한 개만 넣어준 것.

# 첫번째 동영상 뒷부분 2초, 두번째 동영상 앞부분 2초 합성하기
transition_frames = fps * 2

print('frame_cnt1:',frame_cnt1)
print('frame_cnt2:',frame_cnt2)
print('FPS:',fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 동영상 출력할 때 fourcc필요

print('cap1 width:',w)
print('cap1 height:',h)

# 출력 동영상 객체 생성
out = cv2.VideoWriter('./video/output.avi', fourcc, fps, (w,h))

# # 첫번째 프레임
# while True:
#     ret1, frame1 = cap1.read()

#     if not ret1:
#         break

#     out.write(frame1)

#     cv2.imshow('frame', frame1)
#     cv2.waitKey(20)    

# # 두번째 프레임
# while True:
#     ret2, frame2 = cap2.read()

#     if not ret2:
#         break

#     out.write(frame2)

#     cv2.imshow('frame', frame2)
#     cv2.waitKey(20)

# -> 화면전환없이 원숭이에서 코끼리로 확 바뀜.

#########################
# 첫번째 프레임
for i in range(frame_cnt1 - transition_frames): # 뒷부분 2초 구간 삭제
    ret1, frame1 = cap1.read()

    if not ret1:
        break

    out.write(frame1)

    cv2.imshow('frame', frame1)
    cv2.waitKey(20)

### 합성부분 중요!
######### 왼쪽에서 오른쪽으로 
# for i in range(transition_frames):
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()
    
#     ###############################
#     # w/transition_frames : 가로크기 / 48
#     dx = int(w * i / transition_frames) # 비율 값 곱해주기. dx값은 점점 커진다. 
#     frame = np.zeros((h,w,3), dtype=np.uint8)
#     # **중요** 열 잘라오기
#     frame[:,0:dx,:] = frame2[:,0:dx,:] # 코끼리 영상. 앞부분 보여지는 이미지가 조금씩 비율 커짐. 창의 왼쪽에서부터 코끼리 비율 커짐.
#     frame[:,dx:w,:] = frame1[:,dx:w,:] # 원숭이 영상. 뒷부분 보여지는 이미지가 조금씩 비율 작아짐. 창의 오른쪽으로 원숭이 비율 작아짐.
#     ###############################
#     out.write(frame)
    
#     cv2.imshow('frame', frame)
#     cv2.waitKey()

######### 오른쪽에서 왼쪽으로 
# for i in range(transition_frames):
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()
    
#     ###############################
#     # w/transition_frames : 가로크기 / 48
#     dx = int(w * i / transition_frames) # 비율 값 곱해주기. dx값은 점점 커진다. 
#     frame = np.zeros((h,w,3), dtype=np.uint8)
#     # **중요** 열 잘라오기
#     frame[:,w-dx:w,:] = frame2[:,w-dx:w,:] # 코끼리 영상. 앞부분 보여지는 이미지가 조금씩 비율 커짐. 창의 왼쪽에서부터 코끼리 비율 커짐.
#     frame[:,0:w-dx,:] = frame1[:,0:w-dx,:] # 원숭이 영상. 뒷부분 보여지는 이미지가 조금씩 비율 작아짐. 창의 오른쪽으로 원숭이 비율 작아짐.
#     ###############################
#     out.write(frame)
    
#     cv2.imshow('frame', frame)
#     cv2.waitKey()

######### 위에서 아래로 내려오게 하는 합성 프레임
# for i in range(transition_frames):
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()

#     ###############################
#     # h/transition_frames : 세로크기 / 48
#     dy = int(h * i / transition_frames) # 비율 값 곱해주기. dx값은 점점 커진다. 
#     frame = np.zeros((h,w,3), dtype=np.uint8)
#     # **중요** 행 잘라오기
#     frame[0:dy,:,:] = frame2[0:dy,:,:] # 코끼리 영상. 앞부분 보여지는 이미지가 조금씩 비율 커짐. 창의 왼쪽에서부터 코끼리 비율 커짐.
#     frame[dy:h,:,:] = frame1[dy:h,:,:] # 원숭이 영상. 뒷부분 보여지는 이미지가 조금씩 비율 작아짐. 창의 오른쪽으로 원숭이 비율 작아짐.
#     ###############################
#     out.write(frame)
    
#     cv2.imshow('frame', frame)
#     cv2.waitKey(20)

######### 아래에서 위로 내려오게 하는 합성 프레임
# for i in range(transition_frames):
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()

#     ###############################
#     # h/transition_frames : 세로크기 / 48
#     dy = int(h * i / transition_frames) # 비율 값 곱해주기. dx값은 점점 커진다. 
#     frame = np.zeros((h,w,3), dtype=np.uint8)
#     # **중요** 행 잘라오기
#     frame[h-dy:h,:,:] = frame2[h-dy:h,:,:] # 코끼리 영상. 앞부분 보여지는 이미지가 조금씩 비율 커짐. 창의 왼쪽에서부터 코끼리 비율 커짐.
#     frame[0:h-dy,:,:] = frame1[0:h-dy,:,:] # 원숭이 영상. 뒷부분 보여지는 이미지가 조금씩 비율 작아짐. 창의 오른쪽으로 원숭이 비율 작아짐.
#     ###############################
#     out.write(frame)
    
#     cv2.imshow('frame', frame)
#     cv2.waitKey()

######### 대각선 합성 프레임
# for i in range(transition_frames):
#     ret1, frame1 = cap1.read()
#     ret2, frame2 = cap2.read()
    
#     ###############################
#     # w/transition_frames : 가로크기 / 48
#     dx = int(w * i / transition_frames) # 비율 값 곱해주기. dx값은 점점 커진다. 
#     dy = int(h * i / transition_frames)
#     frame = np.zeros((h,w,3), dtype=np.uint8)
#     # **중요** 
#     # frame[0:dy,0:dx,:] = frame2[0:dy,0:dx,:] # 코끼리 영상. 앞부분 보여지는 이미지가 조금씩 비율 커짐. 창의 왼쪽에서부터 코끼리 비율 커짐.
#     # frame[dy:h,dx:w,:] = frame1[dy:h,dx:w,:] # 원숭이 영상. 뒷부분 보여지는 이미지가 조금씩 비율 작아짐. 창의 오른쪽으로 원숭이 비율 작아짐.
    
#     # 원숭이 고정. 코끼리 영상 덧붙여짐
#     # frame[:,:,:] = frame1[:,:,:]
#     # frame[0:dy,0:dx,:] = frame2[0:dy,0:dx,:]

#     # 코끼리 고정. 원숭이 영상 날라감
#     frame[:,:,:] = frame2[:,:,:]
#     frame[dy:h,dx:w,:] = frame1[dy:h,dx:w,:]
#     ###############################
#     out.write(frame)
    
#     cv2.imshow('frame', frame)
#     cv2.waitKey(20)

######### 디졸브 효과 프레임(fadein, fadeout)
for i in range(transition_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    
    ###############################
    # w/transition_frames : 가로크기 / 48
    frame = np.zeros((h,w,3), dtype=np.uint8)
    # **중요** 
    alpha = 1.0 - i / transition_frames  # alpha값은 점점 커짐.(0~1사이의 값이 나오도록 설정)
    frame = cv2.addWeighted(frame1, alpha, frame2, 1-alpha, 0)
    # frame1은 점점 투명해지고, frame2는 점점 투명도가 사라지고
    ###############################
    out.write(frame)
    
    cv2.imshow('frame', frame)
    cv2.waitKey(20)

# 두번째 프레임
for i in range(transition_frames, frame_cnt2): # 앞부분 2초 구간 삭제
    ret2, frame2 = cap2.read()

    if not ret2:
        break

    out.write(frame2)

    cv2.imshow('frame', frame2)
    cv2.waitKey(20)


cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()