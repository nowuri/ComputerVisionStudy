import cv2 as cv
import numpy as np

img = cv.imread("C:\ComputerVision\source\ch4\soccer.jpg")

# 붓칠한 정보를 표시하는데 쓸 객체 (분할 알고리즘은 원 내용 유지해야 함)
img_show = np.copy(img)

# 사용자의 붓칠에 따라 물체인지 배경인지 정보를 기록할 배열
mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)
mask[:, :] = cv.GC_PR_BGD

BrushSiz = 9
LColor, RColor = (255, 0, 0), (0, 0, 255)


def painting(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img_show, (x, y), BrushSiz, LColor, -1)  # 왼쪽 버튼 클릭 시 파란색
        cv.circle(mask, (x, y), BrushSiz, cv.GC_FGD, -1)  # 붓칠한 곳에 cv.GC_FGD 물체라는 표기를 함
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img_show, (x, y), BrushSiz, RColor, -1)  # 오른쪽 버튼 클릭 시 빨간색
        cv.circle(mask, (x, y), BrushSiz, cv.GC_BGD, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:  # 왼쪽 버튼 클릭하고 이동시 파란색
        cv.circle(img_show, (x, y), BrushSiz, LColor, -1)
        cv.circle(mask, (x, y), BrushSiz, cv.GC_FGD, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:  # 오른쪽 버튼 클릭하고 이동시 빨간색
        cv.circle(img_show, (x, y), BrushSiz, RColor, -1)
        cv.circle(mask, (x, y), BrushSiz, cv.GC_BGD, -1)

    cv.imshow('Painting', img_show)


while (True):
    # 붓칠을 그릴 화면
    cv.namedWindow('Painting')
    cv.setMouseCallback('Painting', painting)

    # 붓칠을 끝내는 것
    while (True):
        if cv.waitKey(1) == ord('q'):  # 붓칠 끝내려면 q
            break

    # mask_save = np.copy(mask)

    # GrabCut 적용 코드
    background = np.zeros((1, 65), np.float64)  # 배경 히스토그램 생성, 0 초기화, 실수 표현, 65개 칸을 가짐
    foreground = np.zeros((1, 65), np.float64)  # 물체 히스토그램 생성, 0 초기화, 실수 표현, 65개 칸을 가짐

    # 실제 분할 수행
    cv.grabCut(img, mask, None, background, foreground, 5, cv.GC_INIT_WITH_MASK)
    mask2 = np.where((mask == cv.GC_BGD) | (mask == cv.GC_PR_BGD), 0, 1).astype('uint8')
    grab = img * mask2[:, :, np.newaxis]

    # 그리는 화면을 닫음
    cv.destroyWindow("Painting")

    # 결과 화면을 보여줌
    cv.namedWindow('Grab cut image')
    cv.imshow('Grab cut image', grab)

    # 반복되는 while 문을 벗어나는 것
    if cv.waitKey() == ord('q'):
        break

    # mask = mask_save
    cv.destroyWindow("Grab cut image")
cv.destroyAllWindows()