# 레이블링 함수
# cv2.connectedComponents(image, labels=None, connectivity=None, ltype=None) => retval, labels
# image: 입력 영상(8비트 1채널), labels: 입력 영상과 같은 크기의 레이블 맵(numpy.ndarray)
# connectivity: 4 또는 8. 기본값은 8 
# ltype: labels 타입(기본값은 cv2.CV_32S) 또는 cv2.CV_16S
# retval: 객체의 개수+1(흰색 덩어리 개수+1), N을 반환하면 객체 개수는 N-1개(흰색 덩어리 개수가 N-1개), 1개는 배경

# cv2.connectedComponentsWithStats(image, labels=None, stats=None, centroids=None,
#                                  connectivity=None, ltype=None) => retval, labels, stats, centroids
# stats: 바운딩 박스 - 어느 위치에 어느정도의 크기로 존재하는지, 전체 픽셀 개수를 담고 있는 행렬
# stats의 shape = (N, 5), dtype=numpy.int32 - 전체 객체 개수(N)의 x,y,w,h,면적(5)
# centroids: 각 객체의 중심 위치 정보를 담고 있는 행렬
# centroids의 shpae = (N, 2), dtype=numpy.float64 - 전체 객체 개수(N)의 x,y좌표(2)
# 나머지 파라미터는 위와 동일

import cv2, sys, numpy as np

mat = np.array([
    [0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]], np.uint8)

cnt, labels = cv2.connectedComponents(mat)

print('sep:', mat, sep='\n')
print('cnt:', cnt)
print('labels:', labels, sep='\n')