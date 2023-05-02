import cv2 as cv
import numpy as np

img = cv.imread("C:\ComputerVision\source\ch4\soccer.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 100,200)

# 경계선을 찾아 contour 객체에 저장
# findContours(이미지, 구멍이 있는 경우 바깥쪽 경계선과 그 안에 있는 구멍의 경계선을 계층적으로 찾는 방식, 경계선을 표현하는 방식)
# cv.RETR_LIST = 맨 바깥쪽 경계선만 찾도록 지시
# cv.CHAIN_APPROX_NINE = 모든 점을 기록
contour, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

# 길이가 50 이상인 경계선만 골라 lcontour객체에 저장
lcontour=[]
for i in range(len(contour)):
    if contour[i].shape[0] > 100:
        lcontour.append(contour[i])

# 영상에 경계선을 그림
# drawContours(경계선을 그려 넣을 영상, 경계선, 모든 경계선을 그림, 색, 두께)
# 세번째 인수를 양수로 설정 시 = 해당 번호에 해당하는 경계선 하나만 그림
cv.drawContours(img, lcontour,-1, (0,255,0), 3)
img = cv.resize(img,(500,500))
canny = cv.resize(canny,(500,500))
cv.imshow('Original with contours', img)
cv.imshow('Canny', canny)

cv.waitKey()
cv.destroyAllWindows()
