import sys, cv2, numpy as np

# src = cv2.imread('./images/traffic_light.jpg')
# src = cv2.imread('./images/traffic_light2.jpg')
# src = cv2.imread('./images/traffic_light3.png')
src = cv2.imread('./project/color_circle.jpg')
if src is None:
    print('Image load failed')
    sys.exit()

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (0,0), 1.0)

# 원 검출 
# 바뀌는 부분
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, param1 = 120, param2 = 30, minRadius = 70, maxRadius = 120)
dst = src.copy()
if circles is not None:
    print(circles.shape)
    print(circles)
    for i in range(circles.shape[1]):
        cx, cy, radius = circles[0][i]
        cv2.circle(dst, (cx,cy), radius, 255, 3, cv2.LINE_AA)

        x1 = int(cx-radius)
        y1 = int(cy-radius)
        x2 = int(cx+radius)
        y2 = int(cy+radius)
        radius = int(radius)

        crop = dst[y1:y2, x1:x2, :]
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

        # cv2.imshow('crop', crop)
        # cv2.imshow('mask', mask)
        # cv2.waitKey()
        # cv2.destroyWindow('crop')
        # cv2.destroyWindow('mask')

        # 바뀌는 부분
        color = 'none'
        if 0 < mean_hue < 50:
            color = 'red'
        elif 100 < mean_hue < 120:
            color = 'green'
        cv2.putText(dst, color, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 0.75, 0, 2, cv2.LINE_AA)

cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()