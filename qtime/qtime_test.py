from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time

# qtimer的用法
# 构造时，必须传入一个QObject对象
# 定义的槽函数，必须是传入的OObject对象的方法
# 使用shart()启动

class MyObject(QObject):
    def __init__(self):
        super().__init__()

    def print_time(self):
        print('current time: {}'.format(time.ctime(time.time())))

if __name__=='__main__':
    # 定义一个应用程序
    app = QApplication([])

    myobject = MyObject()
    # 定义一个qtimer定时器
    timer = QTimer(myobject)
    timer.timeout.connect(myobject.print_time)
    timer.start(1000)
    app.exec()