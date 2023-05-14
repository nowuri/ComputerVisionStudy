import cv2 as cv
import numpy as np
import time

# 모델 영상 지정
img1 = cv.imread("C:\ComputerVision\source\ch5\mot_color70.jpg")[190:350,440:560]
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

# 장면 영상 지정
img2 = cv.imread("C:\ComputerVision\source\ch5\mot_color83.jpg")
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# 각 영상에서 SIFT 특징점 검출 후 기술자 추출
sift = cv.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)
print('특징점의 개수: ',len(kp1), len(kp2))

start= time.time()

# flann_matcher 객체 생성 (FLANN 라이브러리 이용)
flann_matcher = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)

# flann_matcher의 knnMatch 함수 호출
# des1, des2 매칭하여 최근접 2개만 찾으라는 의미
knn_match = flann_matcher.knnMatch(des1, des2, 2)
print(len(knn_match))

# 찾은 매칭 쌍 중 최근접 이웃거리 비율 전략을 이용해 좋은 쌍을 골라냄
T = 0.7
good_match=[]
for nearest1, nearest2 in knn_match:
    if(nearest1.distance/nearest2.distance)< T:
        good_match.append(nearest1)
print('매칭에 걸린 시간: ', time.time()-start)

# 두 영상을 나란히 배치하는데 쓸 배열
img_match = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1] + img2.shape[1], 3), dtype= np.uint8)

# 두 영상에 특징점을 표시하고 good_match가 가진 좋은 매칭 쌍을 선으로 연결하여 표시
cv.drawMatches(img1, kp1, img2, kp2, good_match, img_match, flags = cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

cv.imshow('Good Matches', img_match)

cv.waitKey()
cv.destroyAllWindows()