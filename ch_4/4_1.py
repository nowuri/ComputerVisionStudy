import cv2 as cv

img = cv.imread("C:\ComputerVision\source\ch4\soccer.jpg")

# 컬러 영상 -> 명암 영상
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.resize(gray, dsize = (0,0), fx = 0.3, fy = 0.3)

# sobel 함수, x 방향 연산자 적용 => 수직 방향 에지가 더 선명해짐
# cv.Sobel(영상, 결과 영상을 32bit 실수 맴에 저장, x 방향 연산자 , x 방향 연산자, 3X3 크기 사용 지정)
grad_x = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize = 3)

# sobel 함수, y 방향 연산자 적용 => 수평 방향 에지가 더 선명해짐
# cv.Sobel(영상, 결과 영상을 32bit 실수 맴에 저장, y 방향 연산자 , y 방향 연산자, 3X3 크기 사용 지정)
grad_y = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize = 3)

# 음수가 포함된 맵에 절댓값을 취해 양수로 변환
# convertScaleAbs(): 부호 없는 8bit 형 CV_8U를 만듦, 크기가 0보다 작으면 0으로, 255를 넘으면 255로 바꿔 기록
sobel_x = cv.convertScaleAbs(grad_x)
sobel_y = cv.convertScaleAbs(grad_y)

# addWeighted(img1, a, img2, b, c): img1xa + img2xb + c 계산
# img1, 2가 같은 데이터형이어야 함
edge_strength = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5,0)

cv.imshow('Original', gray)
cv.imshow('sobelx', sobel_x)
cv.imshow('sobely', sobel_y)
cv.imshow('edgh strength',edge_strength)

cv.waitKey()
cv.destroyAllWindows()