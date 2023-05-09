import cv2 as cv
import numpy as np

img = cv.imread("C:\ComputerVision\source\ch4\soccer.jpg")

# 붓칠한 정보를 표시하는데 쓸 객체 (분할 알고리즘은 원 내용 유지해야 함)
img_show = np.copy(img)

# 사용자의 붓칠에 따라 물체인지 배경인지 정보를 기록할 배열
# 원본 영상과 크기 동일
mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)

# 배경일 것 같음으로 모두 초기화
# cv.GC_BGE = 배경 판정됨(0)| cv.GC_FGD = 물체 판정됨(1)
# cv.GC_PR_GBD = 배경일 것 같음(2) | cv.GC_PRFGD = 물체 일 것 같음(3)
mask[:,:] = cv.GC_PR_BGD

BrushSiz = 9
LColor, RColor =(255,0,0),(0,0,255)

def painting(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img_show,(x,y),BrushSiz, LColor,-1) # 왼쪽 버튼 클릭 시 파란색
        cv.circle(mask,(x,y),BrushSiz, cv.GC_FGD, -1) # 붓칠한 곳에 cv.GC_FGD 물체라는 표기를 함
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img_show, (x,y),BrushSiz, RColor, -1) # 오른쪽 버튼 클릭 시 빨간색
        cv.circle(mask,(x,y),BrushSiz, cv.GC_BGD, -1)
    elif event==cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON: # 왼쪽 버튼 클릭하고 이동시 파란색
        cv.circle(img_show,(x,y),BrushSiz, LColor, -1)
        cv.circle(mask,(x,y), BrushSiz, cv.GC_FGD, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:# 오른쪽 버튼 클릭하고 이동시 빨간색
        cv.circle(img_show,(x,y),BrushSiz, RColor, -1)
        cv.circle(mask,(x,y), BrushSiz, cv.GC_BGD,-1)

    cv.imshow('Painting', img_show)

cv.namedWindow('Painting')
cv.setMouseCallback('Painting',painting)

while(True):
    if cv.waitKey(1) == ord('q'): # 붓칠 끝내려면 q
        break

# GrabCut 적용 코드
background = np.zeros((1,65),np.float64) # 배경 히스토그램 생성, 0 초기화, 실수 표현, 65개 칸을 가짐
foreground = np.zeros((1,65),np.float64) # 물체 히스토그램 생성, 0 초기화, 실수 표현, 65개 칸을 가짐

# 실제 분할 수행
# grabCut(원본 영상, 물체/정보 정보 맵, 관심영역 지정, 배경 히스토그램, 물체 히스토그램, 반복 횟수, 배경/물체를 표시한 맵을 사용하라)
# 관심 영역 지정(ROI)는 None 설정 시 모든 영역을 본다.
cv.grabCut(img, mask, None, background,foreground, 5, cv.GC_INIT_WITH_MASK)

# 분할한 정보를 가짐
# 배경/배경일 것 같음 => 0, 물체/물체일 것 같음 => 1로 표기하여 mask2 객체에 저장
mask2 = np.where((mask == cv.GC_BGD)|(mask == cv.GC_PR_BGD),0,1).astype('uint8')

# 원본 영상과 곱해서 배경에 해당하는 화소를 검게 바꿔 grab에 저장 후 디스플레이
grab = img*mask2[:,:,np.newaxis]
cv.imshow('Grab cut image',grab)
cv.waitKey()
cv.destroyAllWindows()