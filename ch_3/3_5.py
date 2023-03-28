#감마보정 실험하기
import cv2 as cv
import numpy as np

img = cv.imread("C:\ComputerVision\source\ch3\soccer.jpg")

#사진 사이즈 0.25로 축소
img = cv.resize(img,dsize=(0,0),fx=0.25, fy = 0.25)

def gamma(f, gamma=1.0): # r default 값 = 1.0
    f1 = f/255.0 # L = 256으로 생각 [0,1]로 정규화함
    return np.uint8(255*(f1**gamma)) #255를 곱하고 정수형으로 반환

# 각 이미지를 hstack함수로 이어붙임
gc = np.hstack((gamma(img,0.5),gamma(img,0.75),gamma(img,1.0),gamma(img,2.0),gamma(img,3.0)))
cv.imshow('gamma',gc)

cv.waitKey()
cv.destroyAllWindows()