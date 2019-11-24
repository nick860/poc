from socket import *
import threading
import thread

def handler(clientsock,addr):
    while 1:
        data = clientsock.recv(BUFSIZ)
        if not data:
         print "ending communication with",addr
         break
        msg = 'echoed:... ' + data
        print msg
        clientsock.send(msg)
    clientsock.close()


HOST = '192.168.1.20'
PORT= 11238
print "SERVER PORT NICK: ------>",PORT,"<-------------"  
BUFSIZ = 1024
ADDR=(HOST,PORT)
server_sock = socket(AF_INET,SOCK_STREAM)
server_sock.bind(ADDR)
server_sock.listen(2)

while True:
    print 'Waiting for a client...'
    clientsock, clientaddr = server_sock.accept()
    print 'connection established from:', clientaddr
    thread.start_new_thread(handler, (clientsock, clientaddr))
    
