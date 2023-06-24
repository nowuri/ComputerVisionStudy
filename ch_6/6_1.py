from PyQt5.QtWidgets import *
import sys
import winsound # 삑소리를 내는데 사용

class BeepSound(QMainWindow): # QMainWindow 클래스를 상속 받음 | 윈도우 생성 및 관리
    def __init__(self): # 생성자 함수
        super().__init__()
        self.setWindowTitle('삑 소리 내기')
        self.setGeometry(200,200,500,100)

        # QPushButton 함수로 버튼 3개와 QLabel 함수로 레이블 1개를 만듦
        shortBeepButton=QPushButton('짧게 삑', self)
        longBeepButton=QPushButton('길게 삑', self)
        quitButton=QPushButton('나가기', self)
        self.label=QLabel('환영합니다!',self) #self=멤버변수(클래스 어느 곳에서든 접근 가능, 클래스를 생성한 객체에서도 접근 가능

        # 4개 위젯의 위치와 크기 지정
        shortBeepButton.setGeometry(10,10,100,30)
        longBeepButton.setGeometry(110,10,100,30)
        quitButton.setGeometry(210, 10, 100, 30)
        self.label.setGeometry(10,40,500,70)

        # 버튼을 클릭했을 때 수행할 콜백함수
        shortBeepButton.clicked.connect(self.shortBeepFunction)
        longBeepButton.clicked.connect(self.longBeepFunction)
        quitButton.clicked.connect(self.quitFunction)

    def shortBeepFunction(self):
        self.label.setText('주파수 1000으로 0.5초 동안 삑 소리를 냅니다.')
        winsound.Beep(1000, 500)

    def longBeepFunction(self):
        self.label.setText('주파수 1000으로 3초 동안 삑 소리를 냅니다')
        winsound.Beep(1000,3000)

    def quitFunction(self):
        self.close()

app = QApplication(sys.argv) # PyQt 실행에 필요한 객체 app을 생성
win = BeepSound() # BeepSound 클래스의 객체 win을 생성, __init__ 자동 실행(생성자 함수)
win.show()
app.exec_() # 무한루프 방지, 자동 종료 방지