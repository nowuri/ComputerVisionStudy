import cv2 as cv
import sys

img = cv.imread("C:\ComputerVision\source\ch2\girl_laughing.jpg")

if img is None:
    sys.exit("파일을 읽을 수 없습니다")

def draw(event, x, y, flags, param):
    global ix, iy

    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img,(x,y),(x+200,y+200),(0,0,255),2)
    elif event == cv.EVENT_RBUTTONDOWN: # 오른쪽 마우스를 누르면 원의 중심을 잡음
        ix, iy = x,y
    elif event == cv.EVENT_RBUTTONUP: # 오른쪽 마우스를 떼면 그만큼의 반지름을 계산해 원을 그려줌
        cv.circle(img,(ix, iy),x-ix,(255,0,0),2)

    cv.imshow('Drawing',img)

cv.namedWindow('Drawing')
cv.imshow('Drawing',img)

cv.setMouseCallback('Drawing',draw)

while(True):
    if cv.waitKey(1) == ord('q'):
       cv.destroyAllWindows()
       break