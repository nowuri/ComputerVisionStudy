import cv2 as cv

img = cv.imread("C:\ComputerVision\source\ch4\soccer.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

canny1 = cv.Canny(gray, 50, 150) # Tlow = 50, Thigh = 150 설정
canny2 = cv.Canny(gray, 100, 200) # Tlow = 100, Thigh = 200 설정
canny3 = cv.Canny(gray, 50, 150, 5)
canny4 = cv.Canny(gray, 50, 150, True)

# 사이즈 설정
gray = cv.resize(gray, (300,300))
canny1 = cv.resize(canny1, (300,300))
canny2 = cv.resize(canny2,(300,300))
canny3 = cv.resize(canny3,(300,300))
canny4 = cv.resize(canny4,(300,300))

cv.imshow('Original', gray)
cv.imshow('Canny1', canny1)
cv.imshow('Canny2', canny2)
cv.imshow('Canny3', canny3)
cv.imshow('Canny4', canny4)

cv.waitKey()
cv.destroyAllWindows()
