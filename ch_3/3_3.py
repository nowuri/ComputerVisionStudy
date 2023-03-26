# 오츄 알고리즘으로 이진화하기
import cv2 as cv
import sys

# # threshold(영상 부분과 채널, 명암값의 범위 최소, 명암값의 범위 최대, 오츄 알고리즘)
# # threshold: 알고리즘이 찾은 최적의 임곗값(t)과 이진화된 영상 반환(bin_img)

img = cv.imread("C:\ComputerVision\source\ch3\soccer.jpg")
t, bin_img = cv.threshold(img[:,:,2],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print('오츄 알고리즘이 찾은 최적 임곗값 = ',t)

cv.imshow('R channel',img[:,:,2])
cv.imshow('R channel binarization',bin_img)

cv.waitKey()
cv.destroyAllWindows()