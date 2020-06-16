import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST=socket.gethostname()
PORT=1235
soc.bind((HOST, PORT))

while True:
    dat, addr = soc.recvfrom(1024)
    message = "{} from {}".format(dat, addr)
    print(message)