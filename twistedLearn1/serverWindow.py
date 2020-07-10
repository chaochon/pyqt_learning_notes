from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
app = QApplication(sys.argv)  # your code to init QtCore
import qt5reactor
qt5reactor.install()

from server import SpreadFactory, TCP4ServerEndpoint, reactor


class MyWindow(QMainWindow):

    SigWindowToTcp = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent=parent)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("服务器端窗口")

        self.btn1 = QPushButton("发送", self)
        self.btn1.clicked.connect(self.sendMessage)
        self.btn2 = QPushButton("清空", self)

        self.title1 = QLabel("显示", self)
        self.textRecevied = QTextEdit(self)
        self.title2 = QLabel("输入", self)
        self.textSender = QTextEdit(self)

        self.vboxLayout  = QVBoxLayout(self)
        self.hboxLayout = QHBoxLayout(self)

        self.initUI()

    def initUI(self):

        self.vboxLayout.addWidget(self.title1)
        self.vboxLayout.addWidget(self.textRecevied)
        self.vboxLayout.addWidget(self.title2)
        self.vboxLayout.addWidget(self.textSender)

        self.hboxLayout.addWidget(self.btn1)
        self.hboxLayout.addWidget(self.btn2)
        self.vboxLayout.addLayout(self.hboxLayout)

        self.setLayout(self.vboxLayout)

    def sendMessage(self):
        message = self.textSender.toPlainText()
        # self.SigWindowToTcp.emit(message)
        print("send succefully")

    def writeToWidget(self, message):
        print(message)
        self.textRecevied.setText(message)
        print("write to receive window successfully")

if __name__ == '__main__':

    win = MyWindow()
    win.show()

    sys.exit(app.exec())