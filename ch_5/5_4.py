import cv2 as cv
import numpy as np

# 물체 모델 영상을 정함
img1 = cv.imread("C:\ComputerVision\source\ch5\mot_color70.jpg")[190:350, 440: 560]
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

# 장면 영상을 정함
img2 = cv.imread("C:\ComputerVision\source\ch5\mot_color83.jpg")
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# SIFT 특징점을 검출하고 기술자 추출
sift = cv.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

# flann_matcher 객체 생성, FLANN 라이브러리를 사용하도록 지시
flann_matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)

# knnMatch 함수를 호출하여 매칭 수행, des1, des2와 매칭하여 최근점 2개만 찾으라고 지시
knn_match= flann_matcher.knnMatch(des1, des2, 2)

# 최근점 이웃거리 비율 전략을 이용하여 좋은 쌍을 골라냄
# diatance(특징점 거리, queryIdx, trainIdx)
# queryIdx: 모델 영상에서 추출한 특징점 번호, trainIDx: 장면 영상에서 추출한 특징점 번호
T = 0.7
good_match = []
for nearest1, nearest2 in knn_match:
    if (nearest1.distance/nearest2.distance) < T:
        good_match.append(nearest1)

# points1은 모델 영상에서 특징점 좌표, points2는 장면 영상에서 특징점들의 좌표를 나타냄
points1 = np.float32([kp1[gm.queryIdx].pt for gm in good_match])
points2 = np.float32([kp2[gm.trainIdx].pt for gm in good_match])

# 호모그래피 행렬을 추정하여 H에 저장 (RANSAC 알고리즘 수행)
H,_ = cv.findHomography(points1,points2, cv.RANSAC)
h1, w1 = img1.shape[0], img1.shape[1]
h2, w2 = img2.shape[0], img2.shape[1]

# 첫번째 영상을 포함하는 네 구석의 좌표를 box1에 저장
box1 = np.float32([[0,0],[0,h1-2],[w1-1, h1-1], [w1-1, 0]]).reshape(4,1,2)

# 첫번째 영상의 좌표에 호모그래피 행렬 H를 적용하여 두번째 영상으로 투영하고 결과를 box2에 저장
box2 = cv.perspectiveTransform(box1, H)

# polylines 함수로 box2를 두번째 영상에 그림
img2 = cv.polylines(img2,[np.int32(box2)], True, (0,255,0),8)

# 두 영상을 나란히 배치
img_match = np.empty((max(h1, h2), w1+w2,3), dtype = np.uint8)

# 특징점을 표시하고 가장 좋은 매칭 쌍을 선으로 연결해 표시
cv.drawMatches(img1, kp1, img2, kp2, good_match, img_match, flags = cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv.imshow('Matches and Homography', img_match)

k = cv.waitKey()
cv.destroyAllWindows()