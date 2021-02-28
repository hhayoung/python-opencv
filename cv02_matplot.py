import matplotlib.pyplot as plt
import cv2

# 컬러영상 출력
# openCV는 BGR 순서
imgBGR = cv2.imread('./dami.jpg')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off') # 축 없애기
plt.imshow(imgRGB)
# plt.imshow(imgBGR)
plt.show() # q 누르면 창꺼짐

# 그레이 스케일 영상 출력하기
imgGray = cv2.imread('./dami.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(imgGray, cmap='gray') # colop map을 gray로 설정하면 흑백으로 출력됨.
# cmap옵션을 사용하지 않으면 색이 다 빠지긴 하지만 완전한 회색을 위해서는 cmap을 꼭 gray로 설정해줘야 한다.
plt.show()

# 이미지 지정하기
# cv2.imwrite('./dadadadadami.jpg', imgGray)

# subplot을 이용한 영상 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB) # 1행2열중첫번째
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray') # 1행2열중두번째
plt.show()