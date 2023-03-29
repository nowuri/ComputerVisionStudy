import cv2 as cv
import numpy as np

#영상 축소 및 명암 영상 변환
img = cv.imread("C:\ComputerVision\source\ch3\soccer.jpg")
img = cv.resize(img, dsize=(0,0), fx = 0.4, fy = 0.4)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.putText(gray,'soccer',(10,20),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),2)
cv.imshow('Original',gray)

# GaussianBlur 함수 적용
# cv.GaussianBlur(영상, 필터 크기, 표준편차), (표준편차 = 0.0) => 자동으로 추정
smooth = np.hstack((cv.GaussianBlur(gray,(5,5),0.0),cv.GaussianBlur(gray,(9,9),0.0),
                    cv.GaussianBlur(gray,(15,15),0.0)))
cv.imshow('Smooth',smooth)

# 엠보싱 필터 정의
femboss = np.array([[-1.0,0.0,0.0],
                    [0.0,0.0,0.0],
                    [0.0,0.0,1.0]])

# 엠보싱 필터: 오른쪽 아래 화소 - 왼쪽 위 화소 => 음수 발생 가능
# 음수까지 표현할 수 있도혹 int16으로 표기
gray16 = np.int16(gray)

# int16(음수까지 저장한 것)에 128을 더하고 np.clip 함수 적용
emboss = np.uint8(np.clip(cv.filter2D(gray16,-1,femboss)+128,0,255))

# np.clip을 생략했을 때 부작용 확인
emboss_bad = np.uint8(cv.filter2D(gray16,-1,femboss)+128)

# np.int16으로 변환하지 않았을 때 부작용 확인
emboss_worse = cv.filter2D(gray,-1,femboss)

cv.imshow('Emboss',emboss)
cv.imshow('Emboss_bad',emboss_bad)
cv.imshow('Emboss_worse',emboss_worse)

cv.waitKey()
cv.destroyAllWindows()