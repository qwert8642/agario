import socket
import pygame
import time

main_soket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
main_soket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
main_soket.connect(('localhost',10000))

pygame.init()

WIDTH=800
HEIGHT=600
CC=(WIDTH//2,HEIGHT//2)

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('agario 1488')

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            
    main_soket.send('пасхалка 1488'.encode())
    data = main_soket.recv(1024).decode()
    print('получил',data)

pygame.quit()   