#히스토그램 평활화하기
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("C:\ComputerVision\source\ch3\mistyroad.jpg")

# 명암 영상으로 변환 후 디스플레이
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(gray, cmap = 'gray'), plt.xticks([]), plt.yticks([]), plt.show()

# 히스토그램을 구해 디스플레이
# [0,255] 전체 명암 범위 중 0~50은 거의 사용 X, 대부분 100~200 사이 => 영상 흐릿
h = cv.calcHist([gray],[0],None,[256],[0,256])
plt.plot(h,color='r',linewidth = 1), plt.show()

# 히스토그램 평활화 적용 후 디스플레이
equal = cv.equalizeHist(gray)
plt.imshow(equal, cmap = 'gray'), plt.xticks([]), plt.yticks([]), plt.show()

# equal 영상의 히스토그램 구하고 디스플레이
# 이전보다 영상이 평평해짐
h = cv.calcHist([equal],[0],None,[256],[0,256])
plt.plot(h, color='r',linewidth= 1), plt.show()