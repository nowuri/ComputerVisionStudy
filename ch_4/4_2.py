import cv2 as cv

img = cv.imread("C:\ComputerVision\source\ch4\soccer.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny1 = cv.Canny(gray, 50, 150) # Tlow = 50, Thigh = 150 설정
canny2 = cv.Canny(gray, 100, 200) # Tlow = 100, Thigh = 200 설정

# 사이즈 설정
canny1 = cv.resize(canny1, (500,500))
canny2 = cv.resize(canny2,(500,500))

cv.imshow('Original', gray)
cv.imshow('Canny1', canny1)
cv.imshow('Canny2', canny2)

cv.waitKey()
cv.destroyAllWindows()
