## edge와 hough변환을 이용한 차선 검출

import sys, cv2, numpy as np

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
def canny(img, low_threshold, high_threshold):
    return cv2.Canny(img, low_threshold, high_threshold)
def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
def region_of_interest(img, vertices, color3=(255,255,255), color1=255):
    mask = np.zeros_like(img)
    if len(img.shape) > 2:
        color = color3
    else:
        color = color1
    cv2.fillPoly(mask, vertices, color)
    ROI_image = cv2.bitwise_and(img, mask)
    return ROI_image
def draw_lines(img, lines, color=[0,0,255], thickness=2):
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1,y1), (x2,y2), color, thickness)
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img
def weighted_img(img, initial_img, alpha=1, beta=1., gamma=0.):
    return cv2.addWeighted(initial_img, alpha, img, beta, gamma)

cap = cv2.VideoCapture('./project/road.mp4')
# cap = cv2.VideoCapture('./project/driving.mp4')
if not cap.isOpened():
    print('Video open failed')
    sys.exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2] # 이미지 높이, 너비

    gray_img = grayscale(frame)
    blur_img = gaussian_blur(gray_img, 3)
    canny_img = canny(blur_img, 70, 210) # 비율을 1:2나 1:3 추천

    # 사다리꼴 모형의 Points
    vertices = np.array([[(50, height), (width/2-45, height/2+40), (width/2+120, height/2+40), (width, height)]], dtype=np.int32)
    # vertices = np.array([[(50, height), (width/2-100, height/2+40), (width/2+50, height/2+40), (width-50, height)]], dtype=np.int32)

    ROI_img = region_of_interest(canny_img, vertices)

    hough_img = hough_lines(ROI_img, 1, 1 * np.pi/180, 30, 10, 20)

    dst = weighted_img(hough_img, frame)

    cv2.imshow('frame', frame)
    cv2.imshow('ROI', ROI_img)
    cv2.imshow('dst', dst)

    if cv2.waitKey(100) == 27:
        break

cap.release()
cv2.destroyAllWindows()
