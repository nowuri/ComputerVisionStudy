import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# img = cv.imread("C:\ComputerVision\source\ch3\soccer.jpg")
#
# calcHist(영상, 영상의 채널 번호, 히스토그램 구할 영역, 히스토그램 칸 수, 명함 값의 범위)
# 영상 채널 번호 2 = R 채널, None = 영상의 전체 영역
h = cv.calcHist([img],[2],None,[256],[0,256])
plt.plot(h, color = 'r', linewidth = 1)
plt.show()
