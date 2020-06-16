import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 1234
s.bind((host, port))                         # socket绑定端口
s.listen(5)                                  # 监听 排队容量

while True:
    conn, addr= s.accept()                   # 阻塞， 完成tcp链接，返回新建socket对象
    print("got connect from {}".format(addr))
    messge = "thank you for your connection"
    conn.send(messge.encode('utf-8'))        # 发送字符串
    conn.close()
