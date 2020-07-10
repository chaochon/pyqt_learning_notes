from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class A(QObject):
    signaA = pyqtSignal(str)

    def send(self, s = "caochong"):
        self.signaA.emit(s)

class B(QObject):
    def slot(self, ss):
        print("my name is:{}".format(ss))

if __name__=='__main__':
    a = A()
    b = B()

    a.signaA.connect(b.slot)

    a.send("nihao caochong")