import socket
s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
while True:
    c, addr= s.accept()
    print("got connect from {}".format(addr))
    messge = "thank you for your connection"
    c.send(messge.encode('utf-8'))
    c.close()
