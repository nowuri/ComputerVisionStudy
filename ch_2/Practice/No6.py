import cv2 as cv
import sys

img = cv.imread("C:\ComputerVision\source\ch2\girl_laughing.jpg")

if img is None:
    sys.exit("파일을 열 수 없습니다")

cv.rectangle(img,(830,30),(1000,200),(0,0,255),2)
cv.putText(img,'laugh',(700,24),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
cv.arrowedLine(img,(790,24),(820,29),(0,0,255),2) # 사각형을 가리키는 화살표를 그림

cv.imshow('Draw',img)
cv.waitKey()
cv.destroyAllWindows()