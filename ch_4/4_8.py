import skimage
import numpy as np
import cv2 as cv

orig = skimage.data.horse() # 말이 차지하는 영역은 False, 배경은 True로 표시한 영상
img = 255-np.uint8(orig)*255
cv.imshow('Horse',img)

# 물체의 경계선을 추출하여 contours 객체에 저장
contours,hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

# 경계선을 표시하고 윈도우에 디스플레이
img2 = cv.cvtColor(img, cv.COLOR_GRAY2BGR) # 명암 영상을 컬러 영상으로 바꿈
cv.drawContours(img2, contours, -1,(255,0,255),2) # 경계선 표기(표기할 영상, 경계선, 전체 표기, 색, 두께)
cv.imshow('Horse with contour', img2)

contour = contours[0]

m = cv.moments(contour) # 모멘트 추출하여 m에 저장
area = cv.contourArea(contour) # 경계선으로 둘러싸인 영역의 면적 계산
cx, cy = m['m10']/m['m00'], m['m01']/m['m00'] # 중점 계산
perimeter = cv.arcLength(contour,True) # 둘레의 길이 계산, True = 폐곡선임을 알림
roundness=(4.0*np.pi*area)/(perimeter*perimeter) # 둥근 정도 계산
print('면적= ',area, '\n중점 = (',cx,',',cy,')', '\n둘레= ',perimeter,'\n 둥근 정도 = ', roundness)

# 직선 근사 결과와 convex hull을 컬러로 표기
img3 = cv.cvtColor(img, cv.COLOR_GRAY2BGR) #명암영상으로 변환

contour_approx=cv.approxPolyDP(contour, 8, True) # 경계선을 직선으로 근사 (contour 객체, 임곗값, 폐곡선임을 알림)
cv.drawContours(img3, [contour_approx], -1, (0,255,0),2)

hull = cv.convexHull(contour) # 볼록 헐을 구해 hull 객체에 저장
hull = hull.reshape(1, hull.shape[0], hull.shape[2])
cv.drawContours(img3,hull,-1,(0,0,255),2)

cv.imshow('Horse with line segemtns and convex hull', img3)

cv.waitKey()
cv.destroyAllWindows()