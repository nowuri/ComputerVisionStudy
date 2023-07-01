from PyQt5.QtWidgets import *
import cv2 as cv
import numpy as np
import winsound
import sys

class Panorama(QMainWindow):
    def __init__(self): # 생성자 함수
        super().__init__()
        # 윈도우의 제목, 위치, 크기 설정
        self.setWindowTitle('파노라마 영상')
        self.setGeometry(200,200,700,200)

        # QPushButton 함수로 버튼 5개, QLabel 함수로 레이블 1개를 만듦
        collectButton = QPushButton('영상 수집',self)
        self.showButton = QPushButton('영상 보기',self)
        self.stitchButton = QPushButton('봉합',self)
        self.saveButton = QPushButton('저장',self)
        quitButton = QPushButton('나가기',self)
        self.label = QLabel('환영합니다!',self)

        collectButton.setGeometry(10,25,100,30)
        self.showButton.setGeometry(110,25,100,30)
        self.stitchButton.setGeometry(210,25,100,30)
        self.saveButton.setGeometry(310,25,100,30)
        quitButton.setGeometry(450,25,100,30)
        self.label.setGeometry(10,70,600,170)

        # 비활성으로 설정하여 클릭할 수 없게 함(∵영상 수집이 끝나여 수행할 수 있는 단계)
        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.saveButton.setEnabled(False)

        # 버튼의 콜백함수 등록
        collectButton.clicked.connect(self.collectFunction)
        self.showButton.clicked.connect(self.showFunction)
        self.stitchButton.clicked.connect(self.stitchFunction)
        self.saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)

    def collectFunction(self):
        # <영상 보기>, <봉합>, <저장> 버튼을 비활성화
        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.saveButton.setEnabled(False)
        self.label.setText('c를 여러번 눌러 수집하고 끝나면 q를 눌러 비디오를 끕니다.')

        # 비디오 실행 및 영상 수집
        self.cap = cv.VideoCapture(0,cv.CAP_DSHOW)
        if not self.cap.isOpened(): sys.exit('카메라 연결 실패')

        self.imgs=[]
        while True:
            ret, frame = self.cap.read()
            if not ret: break

            cv.imshow('video display', frame)

            key = cv.waitKey(1)
            if key == ord('c'): # c를 누를 때마다 영상을 imgs에 추가
                self.imgs.append(frame)
            elif key == ord('q'): # q를 누르면 비디오 연결을 끊고 윈도우를 닫고 루프를 빠져나감
                self.cap.release()
                cv.destroyWindow('video display')
                break

        # 수집한 영상이 두장 이상이면 <영상 보기>, <봉합>, <저장> 버튼을 활성화
        if len(self.imgs) >= 2:
            self.showButton.setEnabled(True)
            self.stitchButton.setEnabled(True)
            self.saveButton.setEnabled(True)

    # 수집된 영상의 수를 레이블에 표시
    # 수집된 영상을 0.25배로 축소 후 hstack 함수로 이어붙임
    # 이어붙인 영상을 디스플레이
    def showFunction(self):
        self.label.setText('수집된 영상은 ' + str(len(self.imgs)) + '장입니다.')
        stack = cv.resize(self.imgs[0], dsize=(0,0), fx = 0.25, fy=0.25)
        for i in range(1, len(self.imgs)):
            stack = np.hstack((stack,cv.resize(self.imgs[i], dsize = (0,0), fx = 0.25, fy = 0.25)))
        cv.imshow('Image collection', stack)

    def stitchFunction(self):
        stitcher = cv.Stitcher_create() # 영상 봉합에 쓸 객체
        status, self.img_stitched = stitcher.stitch(self.imgs) # 봉합 | 인수: imgs(수집한 영상 저장), 반환값을 각 변수에 저장
        if status == cv.STITCHER_OK: # 성공한 경우, 윈도우를 새로 열어, 파노라마 영상 디스플레이
            cv.imshow('Image stitched panorama', self.img_stitched)
        else: # 실패시, 삑 소리 & 메세지 출력
            winsound.Beep(3000,500)
            self.label.setText('파노라마 제작에 실패했습니다. 다시 시도하세요')

    def saveFunction(self):
        fname = QFileDialog.getSaveFileName(self, '파일 저장','./')
        cv.imwrite(fname[0], self.img_stitched)

    def quitFunction(self):
        self.cap.release()
        cv.destroyAllWindows()
        self.close()

app = QApplication(sys.argv)
win = Panorama()
win.show()
app.exec_()