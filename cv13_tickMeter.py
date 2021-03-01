# 컴퓨터 비전에서 연산 시간 체크의 필요성
# : 컴퓨터 비전은 대용량 데이터를 다루어서 의미있는 최종 결과를 얻어내야 한다. 
# : 이를 위해서는 매 여러 단계를 거치게 되는데, 매 단계에서 병목(Bottleneck)현상이 있는지 체크하는 것은 중요한 과정 중 하나이다.
# : 단계별 연산 시간을 체크하기 위해 사용하는 클래스 : TickMeter()

# 컴퓨터 비전은 여러 단계의 알고리즘을 거쳐야 하는데 
# 어느 단계에서 시간이 너무 오래 걸리면 다른 단계에도 영향을 미치기 때문에
# 그 단계마다의 연산시간을 체크해주는 게 중요하다. 

import sys, cv2
import numpy as np

img = cv2.imread('./images/test_img.jpg')

if img is None:
    print('Image load failed')
    sys.exit()

# 특정 연산에 대한 시간 측정하기

# 객체 만들어주기
tm = cv2.TickMeter()

tm.reset()
tm.start()

# 이미지가 커서 edge연산
edge = cv2.Canny(img, 50, 150)

tm.stop()
print('Elapsed time: {}ms'.format(tm.getTimeMilli())) # 79.4737ms = 0.08초
# 영상은 초당 프레임이 보통 24인데 프레임마다 이 시간이 걸린다면, 전체 영상은 엄청 오래 걸릴 것.
# 어떤 프레임에서 너무 오랜 시간이 걸린다면 그 프레임에 이상이 있을 수 있다. 그걸 해결해줘야 한다. 
