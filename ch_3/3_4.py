import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
# png 파일에는 4개의 채널이 있음 => IMREAD_UNCHANGED 인수를 넣어 모든 채널을 읽어오도록

img = cv.imread("C:\ComputerVision\source\ch3\JohnHancocksSignature.png",cv.IMREAD_UNCHANGED)

# 4개의 채널 중 3번 채널에 서명 존재
# bin_img = 오츄 이진화를 적용한 값 넣음
t, bin_img = cv.threshold(img[:,:,3],0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

# cmap = gray로 명암 영상 출력, xticks/yticks = x, y축에 눈금을 나타냄
plt.imshow(bin_img, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

# 영상의 일부를 자름
b=bin_img[bin_img.shape[0]//2:bin_img.shape[0],0:bin_img.shape[0]//2+1]
plt.imshow(b,cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

se = np.uint8([[0,0,1,0,0],
               [0,1,1,1,0],
               [1,1,1,1,1],
               [0,1,1,1,0],
               [0,0,1,0,0]])

# iterations = 적용 회수
b_dilation = cv.dilate(b, se, iterations = 1)
plt.imshow(b_dilation,cmap='gray'), plt.xticks([]),plt.yticks([])
plt.show()

b_erosion = cv.erode(b, se, iterations=1)
plt.imshow(b_erosion, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

b_closing = cv.erode(cv.dilate(b, se, iterations=1),se,iterations=1)
plt.imshow(b_closing, cmap='gray'),plt.xticks([]), plt.yticks([])
plt.show()