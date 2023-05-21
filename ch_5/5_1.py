import cv2 as cv
import numpy as np

# 입력 영상 생성
img = np.array([[0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,1,0,0,0,0,0,0],
                [0,0,0,1,1,0,0,0,0,0],
                [0,0,0,1,1,1,0,0,0,0],
                [0,0,0,1,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],z
                [0,0,0,0,0,0,0,0,0,0]], dtype = np.float32) # 실수 연산이 일어나도록 함

# 1X3, 3X1의 미분을 위한 필터
ux = np.array([[-1,0,1]])
uy = np.array([-1,0,1]).transpose()

# 3X3 가우시안 필터를 만듦
k = cv.getGaussianKernel(3,1)
g = np.outer(k,k.transpose())

# dx, dy를 구함
dy = cv.filter2D(img, cv.CV_32F,uy)
dx = cv.filter2D(img, cv.CV_32F,ux)

# dy2, dx2 dydx를 구함
dyy = dy*dy
dxx = dx*dx
dyx = dy*dx

# G * dy2, G* dx2, G*dydx
gdyy = cv.filter2D(dyy, cv.CV_32F,g)
gdxx = cv.filter2D(dxx, cv.CV_32F,g)
gdyx = cv.filter2D(dyx, cv.CV_32F, g)

# 특징 가능성 맵 C를 계산
C = (gdyy*gdxx - gdyx*gdyx) - 0.04*(gdyy+gdxx)*(gdyy+gdxx)

# 극점이 되려면 C가 0.1보다 커야 하며 8개의 이웃보다 커야 함
for j in range(1, C.shape[0]-1): #비최대 억제
    for i in range(1, C.shape[1]-1):
        if C[j,i]>0.1 and sum(sum(C[j,i]>C[j-1:j+2, i-1:i+2])) == 8:
            img[j,i] = 9 #특징점을 원본 영상에 9로 표시

np.set_printoptions(precision=2) # 소수점이하 두 자리까지 출력 설정
print(dy)
print(dx)
print(dyy)
print(dxx)
print(dyx)
print(gdyy)
print(gdxx)
print(gdyx)
print(C) # 특징 가능성 맵
print(img)  # 특징점을 9로 표시한 원본 영상


popping = np.zeros([160,160],np.uint8) # 화소 확인 가능하게 16배로 확대
for j in range(0,160):
    for i in range(0,160):
        popping[j,i] = np.uint8((C[j//16, i//16] + 0.06)*700)


cv.imshow('Image Display2', popping)
cv.waitKey()
cv.destroyAllWindows()