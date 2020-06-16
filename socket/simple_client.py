import socket
s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))
print(s.recv(1024).decode('utf-8'))
s.close()