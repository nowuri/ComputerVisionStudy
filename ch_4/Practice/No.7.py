import cv2 as cv

img = cv.imread("C:\ComputerVision\source\ch4\soccer.jpg")

# 컬러 영상 -> 명암 영상
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.resize(gray, dsize = (0,0), fx = 0.3, fy = 0.3)

# Scharr 함수 (입력 이미지, 출력 이미지 데이터 타입, dx, dy)
# dx, dy: x, y 방향 미분 차수
grad_x = cv.Scharr(gray, -1, 1, 0)
grad_y = cv.Scharr(gray, -1, 0 ,1)

# 음수가 포함된 맵에 절댓값을 취해 양수로 변환
# convertScaleAbs(): 부호 없는 8bit 형 CV_8U를 만듦, 크기가 0보다 작으면 0으로, 255를 넘으면 255로 바꿔 기록
scharr_x = cv.convertScaleAbs(grad_x)
scharr_y = cv.convertScaleAbs(grad_y)

# addWeighted(img1, a, img2, b, c): img1xa + img2xb + c 계산
# img1, 2가 같은 데이터형이어야 함
edge_strength = cv.addWeighted(scharr_x, 0.5, scharr_y, 0.5,0)

cv.imshow('Original', gray)
cv.imshow('scharr_x', scharr_y)
cv.imshow('scharr_y', scharr_y)
cv.imshow('edgh strength',edge_strength)

cv.waitKey()
cv.destroyAllWindows()