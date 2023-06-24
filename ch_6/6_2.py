from PyQt5.QtWidgets import *
import sys
import cv2 as cv

class Video(QMainWindow):
    def __init__(self): # Video 클래스의 생성자 함수
        super().__init__()
        self.setWindowTitle('비디오에서 프레임 수집')
        self.setGeometry(200,200,500,100) # 화면에 나타날 윈도우의 위치와 크기 설정

        # QPushButton 함수로 버튼 4개를 만듦
        videoButton=QPushButton('비디오 켜기', self)
        captureButton = QPushButton('프레임 잡기',self)
        saveButton=QPushButton('프레임 저장',self)
        quitButton=QPushButton('나가기', self)

        # 버튼의 위치와 크기를 지정
        videoButton.setGeometry(10,10,100,30)
        captureButton.setGeometry(110,10,100,30)
        saveButton.setGeometry(210,10,100,30)
        quitButton.setGeometry(310,10,100,30)

        # 사용자가 버튼을 클릭했을 때 수행할 콜백함수 지정
        videoButton.clicked.connect(self.videoFunction)
        captureButton.clicked.connect(self.captureFunction)
        saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)

    # OpenCV 웹캠으로부터 비디오를 입력 받아 윈도우에 디스플레이
    def videoFunction(self):
        self.cap = cv.VideoCapture(0,cv.CAP_DSHOW) # 웹캠과 연결 시도
        if not self.cap.isOpened(): self.close() # 연결 실패 시, 오류 메세지 출력 후 프로그램 끝냄

        while True: # 비디오에서 프레임 획득 후 frame 변수 저장, video display 윈도우에 표시
            ret, self.frame = self.cap.read() #
            if not ret:break
            cv.imshow('video display', self.frame)
            cv.waitKey(1)

    def captureFunction(self):
        self.capturedFrame = self.frame # 비디오 프레임을 저장한 frame을 capturedFrame 변수에 저장
        cv.imshow('Captured Frame', self.capturedFrame) # frame 디스플레이

    def saveFunction(self):
        # 사용자가 파일을 저장할 곳을 브라우징하고 파일 이름을 지정
        # (self, 브라우징 윈도우 제목 지정, 현재 폴더에서 브라우징 하도록)
        frame = QFileDialog.getSaveFileName(self,'파일 저장','./')
        cv.imwrite(frame[0], self.capturedFrame)

    def quitFunction(self):
        self.cap.release() # 비디오 연결을 끊음
        cv.destroyAllWindows() #OpenCV가 연 모든 윈도우를 닫음
        self.close() # 프로그램 종료

app = QApplication(sys.argv)
win=Video()
win.show()
app.exec_()