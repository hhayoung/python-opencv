import sys, cv2, numpy as np

# cap1 = cv2.VideoCapture('./video/blue_screen.mp4')
# if not cap1.isOpened():
#     print('video open failed')
#     sys.exit()

# cap2 = cv2.VideoCapture('./video/monkey2.avi')
# if not cap2.isOpened():
#     print('video open failed')
#     sys.exit()

# w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
# h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
# frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
# frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

# print('frame_cnt1:',frame_cnt1)
# print('frame_cnt2:',frame_cnt2)

# fps = cap1.get(cv2.CAP_PROP_FPS)
# # 두 프레임 사이의 간격
# delay = int(1000 / fps) # 1초가 1000인데 프레임수로 나눠버리면 1초안의 간격이 나옴.

# # 합성 플래그
# composit_flag = False

# while True:
#     ret1, frame1 = cap1.read()

#     if not ret1:
#         break

#     if composit_flag:
#         ret2, frame2 = cap2.read()

#         if not ret2:
#             break
    
#         # frame1 크기로 사이즈 조정
#         frame2 = cv2.resize(frame2, (w,h))

#         # HSV에서 파란색 검출하여 합성
#         hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

#         mask = cv2.inRange(hsv, (100,150,0),(125,255,255))

#         cv2.copyTo(frame2, mask, frame1)
        
#     cv2.imshow('frame1',frame1)
#     key = cv2.waitKey(delay) # 해당 간격의 시작

#     # spacebar를 이용해서 플래그 toggle 시키기
#     if key == ord(' '):
#         composit_flag = not composit_flag
#     elif key == 27:
#         break

# cap1.release()
# cap2.release()
# cv2.destroyAllWindows()

### green_screen 영상으로 실습해보기
cap3 = cv2.VideoCapture('./video/green_screen.mp4')
if not cap3.isOpened():
    print('video open failed')
    sys.exit()
cap4 = cv2.VideoCapture('./video/monkey2.avi')
if not cap4.isOpened():
    print('video open failed')
    sys.exit()

w = round(cap3.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap3.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_cnt3 = round(cap3.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt4 = round(cap4.get(cv2.CAP_PROP_FRAME_COUNT))
fps2 = cap3.get(cv2.CAP_PROP_FPS)

print('frame_cnt3:',frame_cnt3)
print('frame_cnt4:',frame_cnt4)

delay2 = int(1000/fps2)

# 합성 플래그
composit_flag = False

while True:
    ret3, frame3 = cap3.read()
    if not ret3:
        break

    if composit_flag:
        ret4, frame4 = cap4.read()
        if not ret4:
            break

        # frame3 크기로 사이즈 조정
        frame4 = cv2.resize(frame4, (w,h))

        # HSV에서 초록색 검출하여 합성
        hsv = cv2.cvtColor(frame3, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50,150,0),(70,255,255))
        cv2.copyTo(frame4, mask, frame3)

    cv2.imshow('frame3',frame3)
    key = cv2.waitKey(delay2) # 해당 간격의 시작

    # spacebar를 이용해서 플래그 toggle 시키기
    if key == ord(' '):
        composit_flag = not composit_flag
    elif key == 27:
        break

cap3.release()
cap4.release()
cv2.destroyAllWindows()