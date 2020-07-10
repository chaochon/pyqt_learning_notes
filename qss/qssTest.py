from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class WindosDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setProperty("id", "main")
        self.initUI()

        self.setGeometry(0, 0, 800, 600)
        self.move(100, 100)


    def initUI(self):

        # todo: 设置背景bug
        qss = '''
        QWidget#cao{
            background-image: url('./dibala.jpg');
        }
        QPushButton#bottum1{
            color:white; 
            background-color:blue;
        }
        '''


        btn1 = QPushButton()
        btn1.setObjectName("bottum1")
        btn1.setText("按钮1")
        btn2 = QPushButton()
        btn2.setText("按钮2")

        verticalLayout = QVBoxLayout()
        verticalLayout.addWidget(btn1)
        verticalLayout.addWidget(btn2)

        self.setObjectName('cao')
        self.setStyleSheet(qss)
        self.setLayout(verticalLayout)

        self.setWindowOpacity(0.8)   # 设置透明度

        #  设置背景
        # platte = QPalette()
        # platte.setBrush(QPalette.Background, QBrush(QPixmap('./dibala.jpg')))
        # self.setPalette(platte)



if __name__=="__main__":
    app = QApplication(sys.argv)
    windemo = WindosDemo()
    windemo.show()

    sys.exit(app.exec_())