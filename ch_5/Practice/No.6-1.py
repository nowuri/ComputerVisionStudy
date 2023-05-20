import cv2 as cv
import numpy as np

img = cv.imread("C:\ComputerVision\source\ch5\mot_color70.jpg")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

height, width = gray.shape

gaussian = []
gaussian.append(cv.GaussianBlur(gray, (5,5),1.6))
gaussian.append( cv.GaussianBlur(gray,(5,5),2.0159))
gaussian.append( cv.GaussianBlur(gray, (5,5), 2.5398))
gaussian.append(cv.GaussianBlur(gray,(5,5),3.2))
gaussian.append(cv.GaussianBlur(gray,(5,5),4.0317))
gaussian.append(cv.GaussianBlur(gray,(5,5), 5.0797))

DoG =[]
for i in range(5):
    DoG.append(np.zeros_like(gray))

for i in range(height):
    for j in range(width):
        DoG[0][i][j] = float(gaussian[1][i][j]) - float(gaussian[0][i][j])

for i in range(height):
    for j in range(width):
        DoG[1][i][j] = float(gaussian[2][i][j]) - float(gaussian[1][i][j])

for i in range(height):
    for j in range(width):
        DoG[2][i][j] = float(gaussian[3][i][j]) - float(gaussian[2][i][j])

for i in range(height):
    for j in range(width):
        DoG[3][i][j] = float(gaussian[4][i][j]) - float(gaussian[3][i][j])

for i in range(height):
    for j in range(width):
        DoG[4][i][j] = float(gaussian[5][i][j]) - float(gaussian[4][i][j])

for i in range(5):
    pic = DoG[i]
    pic = cv.resize(pic, dsize=(0,0), fx=0.4, fy=0.4)
    cv.imshow('DoG'+str(i), pic);

cv.waitKey()
cv.destroyAllWindows()