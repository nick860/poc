"""NICK"""

from socket import *

host='192.168.1.20'
port=11311
b=1024
addr=(host,port)
tcp=socket(AF_INET,SOCK_STREAM)
tcp.connect(addr)
while 1:

    data=raw_input('>')
    if not data: break
    tcp.send(data)
    data=tcp.recv(1024)
    if not data: break
    print data



tcp.close()
f.close()
"""import _winreg
from socket import *
f=file(r"C:\Python27\Scripts\new8.txt",'w')
import time
time.sleep(11)
f.close()
"""
#this is the code that does all server stuff
"""from socket import *

host='192.168.1.20'
port=11311
b=1024
addr=(host,port)
tcp=socket(AF_INET,SOCK_STREAM)
tcp.connect(addr)
while 1:

    data=raw_input('>')
    if not data: break
    tcp.send(data)
    data=tcp.recv(1024)
    if not data: break
    print data



tcp.close()
f.close()

#this is the code that does all server stuff"""
