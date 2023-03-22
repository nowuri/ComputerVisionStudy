import cv2 as cv
import sys

img = cv.imread("C:\ComputerVision\source\ch2\soccer.jpg")

if img is None:
    sys.exit("파일을 읽을 수 없습니다")

img1 = cv.resize(img,dsize = (0,0),fx = 0.1, fy = 0.1) # 0.1 축소 영상
img2 = cv.resize(img,dsize=(0,0),fx=0.3, fy = 0.3) # 0.3 축소 영상

cv.imshow("Original img",img)
cv.imshow("To_0.1",img1)
cv.imshow("To_0.3",img2)

cv.waitKey()
cv.destroyAllWindows()