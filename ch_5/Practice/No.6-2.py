import cv2 as cv
import numpy as np

img = cv.imread("C:\ComputerVision\source\ch5\mot_color70.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

height, width = gray.shape

n = int(input('가우시안 영상의 개수(최대 6): '))

gaussian = []
num = [1.6, 2.0159, 2.5398, 3.2, 4.0317, 5.0797]

for i in range(n):
    print(num[i])
    gaussian.append(cv.GaussianBlur(gray, (5,5), num[i]))

DoG =[]
for i in range(n):
    DoG.append(np.zeros_like(gray))

for k in range(n-1):
    for i in range(height):
        for j in range(width):
            DoG[k][i][j] = float(gaussian[k+1][i][j]) - float(gaussian[k][i][j])

for i in range(n-1):
    pic = DoG[i]
    pic = cv.resize(pic, dsize=(0,0), fx=0.4, fy=0.4)
    cv.imshow('DoG'+str(i), pic)

cv.waitKey()
cv.destroyAllWindows()
