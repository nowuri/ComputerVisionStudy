import cv2 as cv
import numpy as np
import time

src = np.array([[2,3,3,3,2,2,3,0],
                [3,7,7,7,7,5,4,0],
                [3,7,7,7,7,5,4,3],
                [3,6,7,7,7,5,4,3],
                [3,6,7,7,6,6,4,3],
                [3,6,6,6,4,4,4,3],
                [3,3,4,4,4,2,2,2],
                [3,3,2,2,2,2,2,2]], dtype = np.uint8)

def myEqulizeHist(src):
    a = []

    for i in range(8):
        check = i
        n = 0
        for j in range(8):
            for k in range(8):
                if check == src[j][k]:
                    n = n + 1
        a.append(n / 64.)

    hap = []
    sum = 0
    for i in range(8):
        sum = sum + a[i];
        hap.append(sum)

    hist = []
    for i in range(8):
        hist.append(hap[i] * 7)


start = time.time()
myEqulizeHist(src)
print('myEqualizeHist time: ', time.time()-start)

start = time.time()
cv.equalizeHist(src)
print('OpenCV time: ', time.time()-start)


