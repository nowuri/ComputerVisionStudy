import cv2 as cv

img = cv.imread("C:\ComputerVision\source\ch5\mot_color70.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

frame=[]
for i in range(9):
    sift = cv.SIFT_create(nfeatures=2**(i+1),nOctaveLayers = 3, contrastThreshold = 0.04, edgeThreshold = 10, sigma = 1.6)
    kp,des = sift.detectAndCompute(gray, None)
    gray = cv.drawKeypoints(gray, kp, None, flags = cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    frame.append(gray)

for i in range(1, len(frame)):
    pic = frame[i]
    pic = cv.resize(pic, dsize=(0,0), fx=0.3,fy=0.3)
    cv.imshow('Collected img' + str(i), pic)

cv.waitKey()
cv.destroyAllWindows()