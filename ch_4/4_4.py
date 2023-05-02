import cv2 as cv

img = cv.imread("C:/ComputerVision/source/ch4/apples.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# HoughCircles(명암 영상, 에지 방향 정보 추가 사용하는 알고리즘, 누적 배열의 크기 지정, 원 사이의 최소 거리,
#               캐니 알고리즘의 T(high), 비최대 억제 적용시 사용하는 임계값, 원의 최소 반지름, 원의 최대 반지름)
# 누적 배열의 크기 = 1 일 경우, 입력 영상과 같은 크기 사용
# 원 사이 최소 거리 작을 수록 더 많은 원 검출
apples = cv.HoughCircles(gray, cv.HOUGH_GRADIENT,1, 200,param1=150, param2=20,
                         minRadius=50, maxRadius=120)

for i in apples[0]:
    cv.circle(img,(int(i[0]), int(i[1])),int(i[2]),(255, 0, 0),2)

cv.imshow('Apple detection', img)

cv.waitKey()
cv.destroyAllWindows()
