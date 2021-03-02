import cv2, sys, numpy as np

src = cv2.imread('./images/img_1.png')
if src is None:
    print('Image load failed')
    sys.exit()

# aff = np.array([[1,m,a], [0,1,b]])
# aff = np.array([[1,0,a], [0,m,b]])
aff = np.array([[1,0.5,0], 
                [0,1,0]], dtype=np.float32)

print(src.shape) # (544, 826, 3)
h, w = src.shape[:2]

# dst = cv2.warpAffine(src, aff, (0,0))
dst = cv2.warpAffine(src, aff, (w + int(h*0.5),h))

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()

cv2.destroyAllWindows()