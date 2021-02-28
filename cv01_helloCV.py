import cv2
import sys

print('Hello OpenCV', cv2.__version__)

# 영상파일 불러오기
# img = cv2.imread('./dami.jpg')
# cv2.IMREAD_COLOR      : default. 컬러
# cv2.IMREAD_GRAYSCALE  : 흑백
# cv2.IMREAD_UNCHANGED  : 투명 PNG 파일
img = cv2.imread('./dami.jpg', cv2.IMREAD_UNCHANGED)

if img is None:
    print('Image load failed!!')
    sys.exit()

# image라는 창을 생성
# cv2.namedWindow('image')
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE) # 원래의 이미지 크기대로
# cv2.namedWindow('image', cv2.WINDOW_NORMAL) # 사이즈 조절 가능


# 이미지를 보여주는 곳이 imshow인줄 알았는데, 한 줄씩 디버깅을 해보니까 waitKey()가 있어야지만 해당 이미지가 보여진다.
# imshow()와 waitKey()는 하나의 쌍으로 같이 적어줘야 한다.
cv2.imshow('image', img) # image라는 창에 img를 보여주겠다.
# namedWindow() 코드가 없어도 이미지 창이 뜬다. -> 그대신 자유도가 없음(크기를 조절한다던가)
# imshow에 의해서 생성된 image는 이미지의 크기대로만 생성
cv2.waitKey() # key값이 들어올 때까지 기다리겠다. 실행하고 아무키나 누르면 창이 닫힌다.
# └ 이 코드가 없으면 이미지창이 바로 꺼진다.
# cv2.waitKey(2000) # 2초간 delay를 줌
# key = cv2.waitKey(2000) # 2초간 delay를 줌
# print(key) # 내가 누른 키의 아스키 값을 넘겨줌. 키 값을 활용할 수 있다.

# (활용) 특정 키를 눌러야지만 종료됨.
# while True:
#     # if cv2.waitKey() == 27:
#     if cv2.waitKey() == ord('q'):
#         break

cv2.destroyAllWindows() # 모든 윈도우창을 닫겠다. 
