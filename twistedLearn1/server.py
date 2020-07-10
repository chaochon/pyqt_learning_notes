#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

import pickle

clients = []

class Spreader(Protocol, QObject):

    SignalTcpToWindow = pyqtSignal(str)

    def __init__(self, factory):
        super().__init__()
        self.factory = factory
        self.connect_id = None

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.connect_id = self.factory.numProtocols
        self.transport.write((u"欢迎来到Spread Site, 您是第%d个客户端用户！\n" %
                              (self.connect_id, )).encode('utf8'))
        print("new connect: %d" % self.connect_id)
        clients.append(self)

    def connectionLost(self, reason):
        clients.remove(self)
        print("lost connect: %d" % self.connect_id)

    def dataReceived(self, data):
        d = pickle.loads(data)
        print("received data in server")
        print("data:{}".format(d))
        # send data back
        self.transport.write(pickle.dumps(d, 2))
        print("send back successfully!")


class SpreadFactory(Factory):
    def __init__(self):
        super(SpreadFactory, self).__init__()
        self.numProtocols = 0
        self.protocol = Spreader(self)

    def buildProtocol(self, addr):
        return self.protocol

if __name__=='__main__':

    # 8007是本服务器的监听端口，建议选择大于1024的端口
    endpoint = TCP4ServerEndpoint(reactor, 8007)
    endpoint.listen(SpreadFactory())
    reactor.run()  # 挂起运行
