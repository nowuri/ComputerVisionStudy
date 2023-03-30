import cv2 as cv

img = cv.imread("C:/ComputerVision/source/ch3/rose.png")

# 100 X 100 패치를 잘라 객체에 저장 (원래 영상은 너무 커서)
patch = img[250:350, 170:270,:]

# 오려낸 곳을 파란색 박스로 원 영상에 표기
img = cv.rectangle(img, (170,250),(270,350),(255,0,0),3)

# 최근접 이웃 후 5배 확인
patch1 = cv.resize(patch, dsize=(0,0),fx = 5, fy = 5, interpolation = cv.INTER_NEAREST)

# 양선형보간 방법 후 5배 확인
patch2 = cv.resize(patch, dsize=(0,0),fx = 5, fy = 5, interpolation = cv.INTER_LINEAR)

# 양3차보간 방법 후 5배 확인
patch3 = cv.resize(patch, dsize=(0,0),fx = 5, fy = 5, interpolation = cv.INTER_CUBIC)

cv.imshow('Original',img)
cv.imshow('Resize nearest',patch1)
cv.imshow('Resize bilinear',patch2)
cv.imshow('Resize bicubic',patch3)

cv.waitKey()
cv.destroyAllWindows()