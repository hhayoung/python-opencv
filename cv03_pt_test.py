# 이미지 슬라이드 쇼
import sys
import cv2
import glob

imgs = glob.glob('./images/*.jpg') # images 폴더 밑에 jpg로 끝나는 파일을 다 불러옴
# glob 모듈의 glob 함수는 조건에 맞는 파일명을 리스트 형식으로 반환한다. 
# '*'와 '?'같은 와일드카드만을 지원한다.


for f in imgs:
    print(f) # jpg확장자를 갖는 파일명 출력

# 전체 화면으로 각 image 띄우기
cv2.namedWindow('image', cv2.WINDOW_NORMAL) # 사이즈 조절하려면 cv2.WINDOW_NORMAL
# 전체화면만드는 속성. 옵션을 cv2.WINDOW_NORMAL로 했을 때만 동작한다.
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


cnt = len(imgs)
idx = 0

while True:
    img = cv2.imread(imgs[idx])
    
    if img is None:
        print('Image load failed!!')
        break
    
    cv2.imshow('image', img)
    if cv2.waitKey(1000) >= 0 : # 어떤 키 값이 들어오면 무조건 0보다는 큼
        break
    idx += 1
    if idx >= cnt:  # 무한으로 돌게끔
        idx = 0

cv2.destroyAllWindows()