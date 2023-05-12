import cv2 as cv

img = cv.imread("C:\ComputerVision\source\ch5\mot_color70.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# SIFT 특징점을 추출하는데 쓸 sift 객체를 생성
# 변수: nfeatures = 검출한 특징점 반환 후 지정한 개수 만큼 신뢰도가 높은 순서대로 반환
#      nOctaveLayers = 옥타브 개수 재정
#      contrastThreshold = 테일러 확장으로 미제 조정할 때 쓰는 매개변수, 값이 클수록 적은 수의 특징점 검출
#      edgeThreshold = 에지에서 검출된 특징점을 걸러내는데 쓰는 매개변수, 값이 클수록 덜 걸러내 더 많은 특징점 발생
#      sigma = 옥타브 0의 입력 영상에 적용할 가우시안의 표준 편차
sift = cv.SIFT_create()

# 특징점과 기술자를 각 객체에 저장
# 원의 중심 = 특징점 위치, 반지름 = 스케일, 선분 = 지배적인 방향
kp, des = sift.detectAndCompute(gray, None)

gray = cv.drawKeypoints(gray, kp, None, flags = cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imshow('sift',gray)

cv.waitKey()
cv.destroyAllWindows()
