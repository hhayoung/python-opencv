import math
import cv2

def setLabel(img, pts, label):
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))

def main():
    img = cv2.imread('./images/poly.jpg', cv2.IMREAD_COLOR)    

    if img is None:
        print('Image load failed!')
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 전역이진화
    # star을 잡기 위해서 수동으로 임계치 설정
    _, img_bin = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    # otsu로는 별이 노란색이라 잘 안잡힘.
    # 임계값 설정이 필요하다.

    # 외곽선 검출(가장 외부에 있는 외곽선만)
    contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.imshow('img_bin', img_bin) # 이진화
    # cv2.imshow('gray', gray)

    for pts in contours:
        # 각 외곽선의 면적
        # print(cv2.contourArea(pts))
        if cv2.contourArea(pts) < 300: # 너무 작으면 무시
            continue

        # 외곽선의 근사화
        approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)

        # 꼭지점 개수
        vtc = len(approx)

        convex = cv2.isContourConvex(approx)

        if convex:
            if vtc == 3:
                setLabel(img, pts, 'TRI')
            elif vtc == 4:
                setLabel(img, pts, 'RECT')
            elif vtc == 10:
                setLabel(img, pts, 'STAR')
            elif vtc == 5 or vtc == 6:
                setLabel(img, pts, 'POLY')
            # 원검출
            else:
                length = cv2.arcLength(pts, True)
                area = cv2.contourArea(pts)
                ratio = 4. * math.pi * area / (length * length)

                if ratio > 0.85:
                    setLabel(img, pts, 'CIR') # 원
                elif ratio < 0.85:
                    setLabel(img, pts, 'CIR') # 타원

    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()