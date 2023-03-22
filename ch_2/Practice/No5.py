import cv2 as cv
import sys

cap = cv.VideoCapture(0,cv.CAP_DSHOW)

if not cap.isOpened():
    sys.exit("카메라 연결 실패")

while True:
    ret, frame = cap.read()

    if not ret:
        print("프레임 획득에 실패하여 루프를 나갑니다")
        break;

    cv.imshow("Video display",frame)

    key = cv.waitKey(1)

    if key == ord('q'):
        break
    elif key == ord('g'):
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY) # g 입력 시, 명암 영상 디스플레이
        cv.imshow("Gray video display",gray)
    elif key == ord('c'):
        cv.imshow("Color video display",frame)  # c 입력 시, 컬러 영상 디스플레이

cap.release()
cv.distroyAllWindows()