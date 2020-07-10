import pickle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class A(QObject):

    SigAToB = pyqtSignal(bytes)

    def __init__(self):
        super().__init__()
        self.data = {'a': 1, 'b': 2}

    def send(self):
        dataSent = pickle.dumps(self.data, 2)
        self.SigAToB.emit(dataSent)

class B(QObject):

    def receviedData(self, message):
        data = pickle.loads(message)
        print("recived data:{} in B".format(data))

if __name__=='__main__':

    a = A()
    b = B()
    a.SigAToB.connect(b.receviedData)

    a.send()