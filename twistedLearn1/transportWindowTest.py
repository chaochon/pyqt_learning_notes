from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
app = QApplication(sys.argv)  # your code to init QtCore
import qt5reactor
qt5reactor.install()

from client import *


class MyWindow(QWidget):

    SigWindowToTcp = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent=parent)

        self.setGeometry(100, 100, 800, 600)

        self.btn1 = QPushButton("发送", self)
        self.btn1.clicked.connect(self.sendMessage)
        self.btn2 = QPushButton("清空", self)

        self.title1 = QLabel("一级软件", self)
        self.textRecevied = QTextEdit(self)
        self.title2 = QLabel("二级软件", self)
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
        self.SigWindowToTcp.emit(message)
        print("send succefully")

    def writeToWidget(self, message):
        print(message)
        self.textRecevied.setText(message)
        print("write to receive window successfully")


if __name__=='__main__':

    win = MyWindow()
    win.show()

    factory = EchoClientFactory()

    win.SigWindowToTcp.connect(factory.protocol.sendMessage)
    factory.protocol.SigMessageToWindow.connect(win.writeToWidget)

    host = "127.0.0.1"
    port = 8007
    reactor.connectTCP(host, port, factory)
    reactor.run()

    sys.exit(app.exec_())