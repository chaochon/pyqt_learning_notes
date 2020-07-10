#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet.protocol import Protocol, ClientFactory, Factory
from twisted.internet import reactor
from PyQt5.QtCore import *

class Echo(Protocol, QObject):

    SigMessageToWindow = pyqtSignal(str)

    def __init__(self, id=0):
        super(Echo, self).__init__()
        self.id = id

    def connectionMade(self):
        print("Connected to the server!")

    def dataReceived(self, data):
        print("got message: ", data.decode('utf-8'))
        self.SigMessageToWindow.emit(data.decode('utf-8'))

    def connectionLost(self, reason):
        print("Disconnected from the server!")

    def sendMessage(self, message):
        if self.transport.connected:
            self.transport.write(message.encode('utf-8'))
            print("tcp send successfully, content:{}".format(message))


class EchoClientFactory(ClientFactory):
    def __init__(self):
        super(EchoClientFactory, self).__init__()
        self.protocol = Echo()

    def startedConnecting(self, connector):
        print('Started to connect.')

    def buildProtocol(self, addr):
        print("here in echo")
        return self.protocol

    def clientConnectionLost(self, connector, reason):
        print('Lost connection.  Reason:', reason)

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)

if __name__=='__main__':
    import sys
    host = "127.0.0.1"
    port = 8007
    factory = EchoClientFactory()
    reactor.connectTCP(host, port, factory)
    reactor.run()
