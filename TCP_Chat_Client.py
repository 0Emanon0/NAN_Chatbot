import socket
import time
import threading

host = '192.168.8.120'
port = 5000

server = (host,port)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(server)
s.setblocking(0)
msg=''

Nickname = input('Name: ')
while msg != 'q':
        try:
                data, addr = s.recvfrom(1024)
                print('NAN:'+data.decode('utf-8'))
                msg = input(Nickname+':')
                while msg == '':
                        msg = input(Nickname+':')
                s.sendall(msg.encode('utf-8'))
                time.sleep(0.2)
        except:
                pass
s.close()
