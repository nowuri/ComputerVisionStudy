import cv2 as cv
import numpy as np

img = cv.imread("C:\ComputerVision\source\ch5\mot_color70.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

frame=[]
for i in range(9):
    sift = cv.SIFT_create(nfeatures=2**(i+1),nOctaveLayers = 3, contrastThreshold = 0.04, edgeThreshold = 10, sigma = 1.6)
    kp,des = sift.detectAndCompute(gray, None)

    gray = cv.drawKeypoints(gray, kp, None, flags = cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv.resize(gray, dsize = (0,0),fx=0.2,fy=0.2)
    frame.append(gray)

imgs = frame[0]
for i in range(1, len(frame)):
    imgs = np.hstack((imgs,frame[i]))

print(len(frame))

cv.imshow('Collected img', imgs)
cv.waitKey()
cv.destroyAllWindows()