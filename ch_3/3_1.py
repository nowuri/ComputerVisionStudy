# RGB 컬러 영상을 채널별로 구분해 디스플레이하기

import cv2 as cv
import sys

img = cv.imread("C:\ComputerVision\source\ch3\soccer.jpg")

if img is None:
    sys.exit("파일을 읽을 수 없습니다")

# 원래 영상 디스플레이
cv.imshow('original_RGB',img)

# 왼쪽 위 부분 잘라내기
# 첫 2개 인자 = 크기지정/자르는 것, 마지막 인자 = 컬러 채널
cv.imshow('Upper left half',img[0:img.shape[0]//2, 0:img.shape[1]//2,:])

# 1/4 ~ 3/4에 해당하는 엿앙의 중간 부분 잘라내기
cv.imshow('Center half',img[img.shape[0]//4:3*img.shape[0]//4,img.shape[1]//4:3*img.shape[1]//4,:])

# BGR 순서로 저장 => R = 2, G = 1, B = 0
cv.imshow('R channel',img[:,:,2])
cv.imshow('G channel', img[:,:,1])
cv.imshow('B channel', img[:,:,0])

cv.waitKey()
cv.destroyAllWindows()