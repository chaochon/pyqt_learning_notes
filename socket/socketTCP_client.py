import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 1234

s.connect((host, port))             # 请求建立TCP连接
messageFromServer = s.recv(1024).decode('utf-8')
print(messageFromServer)
s.close()
