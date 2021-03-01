import sys, cv2, numpy as np
import matplotlib.pyplot as plt

# matplotlib말고 opencv로 직접 만들어서 히스토그램 뿌리기
def getHistDraw(hist):
    imgHist = np.full((100,256), 255, dtype=np.uint8) # np.full((세로,가로), 흰색, np.uint8)
    # 가장 높은 높이 100으로 제한

    print(hist.shape) # (256, 1)
    print(np.max(hist)) # 2561.0
    print(hist[50,0]) # 1732.0
    print(hist[55,0]) # 1223.0
    print(int(hist[50,0]/np.max(hist) * 100)) # 67
    print(int(hist[55,0]/np.max(hist) * 100)) # 47
    print(100 - int(hist[50,0]/np.max(hist) * 100)) # 33
    print(100 - int(hist[55,0]/np.max(hist) * 100)) # 53


    '''
    창의 왼쪽기준으로 x → 이고, y ↓  -> 창의 왼쪽 상단 좌표 => (0,0)
    > pt1의 값은 창의 아래 바닥의 좌표 (x,100)
    > pt2 분석
    아래바닥으로부터 pt2값에 해당하는 점을 찍으러 올라와야 하니까 100에서 - 를 해주는 것.
    hist[x,0]인 이유 -> hist.shape을 찍어보면 (256,1) 열이 하나기 때문에 0번째 인덱스밖에 존재하지 않는다.

    예를 들어,
    hist[50,0]의 값은 1732.0
    여기에 histMax(2561.0)로 나누게 되면 
    1732.0 / 2561.0 = 0.676298... -> 그래서 100에서 빼주기 위해 100을 곱해주는 것.(단위 통일)
    100을 곱해서 int로 형변환 해주면 67
    pt2는 (50,100-67) = (50, 33) 좌표가 되고
    cv2.line()함수를 이용해 pt1(50,100)과 pt2(50,33)를 이어주면 직선이 그려지게 된다.
    
    전체의 hist값을 계산해서 직선을 그려주면 하나의 히스토그램이 완성된다.
    '''
    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)  # 아래 바닥에 해당하는 점. 좌측상단에서부터의 좌표
        pt2 = (x, 100 - int(hist[x,0] * 100 / histMax)) # 해당 값에 해당하는 점
        cv2.line(imgHist, pt1, pt2, 0) # 시작점, 마지막점, 검은색
        # pt1와 pt2를 직선으로 이어서 하나하나 그려준 그림
    return imgHist

src = cv2.imread('./images/lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256])
hist_chart = getHistDraw(hist)

cv2.imshow('src',src)
cv2.imshow('hist_chart',hist_chart)
cv2.waitKey()

# plt.plot(hist)
# plt.show()

cv2.destroyAllWindows()