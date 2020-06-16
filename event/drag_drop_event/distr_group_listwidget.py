from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class DragListWidget(QListWidget):
    def __init__(self, parent=None):

        super(DragListWidget, self).__init__(parent=parent)

        # 开启拖动
        self.setDragEnabled(True)
        self.setDragDropMode(self.DragOnly)

        self.resize(400, 400)
        self.move(400, 200)
        self.setWindowTitle("无人平台清单")
        self.init()
        self.show()

    def init(self):

        # 加载营级分配的无人平台清单
        for n in range(10):
            item = QListWidgetItem("无人平台{}".format(n+1), self)
            item.setSizeHint(QSize(10,30))

    def startDrag(self, supportedActions):
        items = self.selectedItems()
        drag = QDrag(self)
        mimeData = self.mimeData(items)
        # 由于QMimeData只能设置image、urls、str、bytes等等不方便
        # 这里添加一个额外的属性直接把item放进去,后面可以根据item取出数据
        mimeData.setProperty('myItems', items)
        drag.setMimeData(mimeData)
        drag.exec_(supportedActions)



class DropListWidget(QListWidget):
    def __init__(self, parent=None):

        super(DropListWidget, self).__init__(parent=parent)

        self.setAcceptDrops(True)

        self.resize(400, 400)
        self.move(800, 200)
        self.setWindowTitle("编组1清单")
        self.init()
        self.show()

    def init(self):
        pass


    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        # 获取拖放的items
        print("here in dropEvent")
        # if event.proposedAction()==Qt.MoveAction:
        #     event.acceptProposedAction()
        items = event.mimeData().property('myItems')
        for item in items:
            self.makeItem(item.text())


    def makeItem(self, name):
        item = QListWidgetItem(name, self)
        item.setSizeHint(QSize(10, 30))


if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    dragWidget = DragListWidget()
    dropWidget = DropListWidget()
    sys.exit(app.exec())