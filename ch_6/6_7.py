import cv2 as cv
import numpy as np
from PyQt5.QtWidgets import *
import sys

class VideoSpecialEffect(QMainWindow):
    def __init__(self): # 생성자 함수
        super().__init__()
        self.setWindowTitle('비디오 특수 효과')
        self.setGeometry(200,200,400,100) # 윈도우 위치, 크기 설정

        # 버튼, 콤보 박스 생성
        videoButton = QPushButton('비디오 시작',self)
        self.pickCombo = QComboBox(self)
        self.pickCombo.addItems(['엠보싱','카툰','연필 스케치(명암)','연필 스케치(컬러)','유화'])
        quitButton = QPushButton('나가기',self)

        # 버튼, 콤보 박스 위치 설정
        videoButton.setGeometry(10,10,140,30)
        self.pickCombo.setGeometry(150,10,110,30)
        quitButton.setGeometry(280,10,100,30)

        # 버튼 콜백 함수 등록
        videoButton.clicked.connect(self.videoSpecialEffectFunction)
        quitButton.clicked.connect(self.quitFunction)

    # 비디오 시작 버튼
    def videoSpecialEffectFunction(self):
        self.cap = cv.VideoCapture(0, cv.CAP_DSHOW) # 웹 캠 연결 시도
        if not self.cap.isOpened(): sys.exit('카메라 연결 실패')

        while True:
            # 실시간 프레임 읽기
            ret, frame = self.cap.read()
            if not ret: break

            # 특수효과 번호 알아냄
            pick_effect = self.pickCombo.currentIndex()
            # 지정된 특수 효과 적용
            if pick_effect == 0: # 엠보싱
                femboss = np.array([[-1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                gray16 = np.int16(gray)
                special_img = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))
            elif pick_effect == 1: # 카툰
                special_img = cv.stylization(frame, sigma_s=60, sigma_r=0.45)
            elif pick_effect == 2: # 연필 스케치(명암)
                special_img, _ = cv.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
            elif pick_effect == 3: # 연필 스케치(컬러)
                _, special_img = cv.pencilSketch(frame, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
            elif pick_effect == 4: # 유화
                special_img = cv.xphoto.oilPainting(frame, 10, 1, cv.COLOR_BGR2Lab)

            # 시스플레이
            cv.imshow('Special effect', special_img)
            cv.waitKey(1)

    # 나가기 버튼 : 웹캠 연결 끊고 윈도우 닫고 프로그램 종료
    def quitFunction(self):
        self.cap.release()
        cv.destroyAllWindows()
        self.close()

app = QApplication(sys.argv)
win = VideoSpecialEffect()
win.show()
app.exec_()