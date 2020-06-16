from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Widget(QWidget):
    def __init__(self, parent=None):

        super(Widget, self).__init__(parent=parent)

        self.setWindowTitle("event")
        self.resize(800, 600)
        self.move(400, 200)
        self.show()

        self.key = ""
        self.text = "caochong"
        self.message = "message at first!"

        self.timer = QTimer.singleShot(5000, self.giveHelp)

    def giveHelp(self):
        self.message = "message after 5 second!"
        self.update()

    # 绘图事件
    def paintEvent(self, event):
        text = self.text
        i = text.find('\n\n')
        if i>0:
            text = text[0:i]
        if self.key:
            text += "\n\n你按下了：{}".format(self.key)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.TextAntialiasing)
        painter.drawText(self.rect(), Qt.AlignCenter, text)

        if self.message:
            painter.drawText(self.rect(), Qt.AlignHCenter | Qt.AlignBottom, self.message)
            QTimer.singleShot(5000, self.clearMessage)
            QTimer.singleShot(5000, self.update)

    def clearMessage(self):
        self.message=""

    # 键盘事件
    def keyPressEvent(self, event):
        self.key = ""
        if event.key() == Qt.Key_Home:
            self.key = "Home"
        elif event.key() == Qt.Key_End:
            self.key = "End"

        if self.key:
            self.update()






if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    wid = Widget()
    sys.exit(app.exec())