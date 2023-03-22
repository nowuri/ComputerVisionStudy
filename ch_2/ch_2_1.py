import cv2 as cv
import numpy as np
import sys

BrushSiz = 5
LColor,RColor = (255,0,0), (0,0,255)
# 콜백 함수
def draw(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),BrushSiz,LColor,-1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),BrushSiz,RColor,-1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img,(x,y),BrushSiz,LColor,-1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img,(x,y),BrushSiz,RColor,-1)

    cv.imshow('Painting',img)

if __name__ == '__main__':
    img = cv.imread("C:\ComputerVision\source\ch2\girl_laughing.jpg")

    if img is None:
        sys.exit("파일을 찾을 수 없습니다")

    cv.namedWindow('Painting') # Drawing의 이름을 가진 새 윈도우를 생성
    cv.imshow('Painting',img)

    cv.setMouseCallback('Painting',draw) # Drawing 윈도우에서 마우스 클릭 일어났을 때 draw 함수 실행

    while(True):
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break