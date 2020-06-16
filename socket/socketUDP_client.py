import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST = socket.gethostname()
PORT = 1235

for i in range(10):
    data = "clientData{}".format(i).encode('utf-8')
    soc.sendto(data, (HOST, PORT))
soc.close()