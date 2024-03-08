import socket
import time

main_soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_soket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
main_soket.connect(('localhost',10000))

while True:
    main_soket.send('пасхалка 1488'.encode())