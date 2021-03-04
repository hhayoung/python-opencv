import sys, cv2, numpy as np

cap = cv2.VideoCapture('./project/Traffic_Light.mp4')
if not cap.isOpened():
    print('Video open failed')
    sys.exit()

fps = cap.get(cv2.CAP_PROP_FPS)

# 비디오 각 프레임 처리
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(0,0), 1.0)

    # 원 검출 
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, param1 = 120, param2 = 50, minRadius = 50, maxRadius = 90)

    if circles is not None:
    #     print(circles.shape)
    #     print(circles)
        for i in range(circles.shape[1]):
            cx, cy, radius = circles[0][i]
            cv2.circle(frame, (cx,cy), radius, (0,0,255), 2, cv2.LINE_AA)

            x1 = int(cx-radius)
            y1 = int(cy-radius)
            x2 = int(cx+radius)
            y2 = int(cy+radius)
            radius = int(radius)

            crop = frame[y1:y2, x1:x2, :]
            ch, cw = crop.shape[:2]

            # 신호등 영역 ROI mask 영상
            mask = np.zeros((ch,cw), np.uint8)
            cv2.circle(mask, (cw//2, ch//2), radius, 255, -1)

            # 색 인식
            hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
            hue, _, _ = cv2.split(hsv)
            hist_shift = (hue + 30) % 180

            mean_hue = cv2.mean(hist_shift, mask)[0]
            print(mean_hue)

            color = 'none'
            if 0 < mean_hue < 60:
                color = 'red'
            elif 70 < mean_hue < 150:
                color = 'green'
            cv2.putText(crop, color, (20,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,255,255), 2, cv2.LINE_AA)

            # cv2.imshow('crop', crop)
            # cv2.imshow('mask', mask)
            cv2.imshow('frame', frame)
    #         if cv2.waitKey(20) == 27:  # ESC키 누르면
    #             break
    #         cv2.destroyWindow('crop')
    #         cv2.destroyWindow('mask')
    if cv2.waitKey(20) == 27:
        break
    # cv2.waitKey()


cap.release()
cv2.destroyAllWindows()