import _winreg
from socket import *
k = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,'Printers\Defaults',0,_winreg.KEY_READ)
info = _winreg.QueryInfoKey(k)
for i in range(info[0]):

               key = _winreg.EnumKey(k,i)
               if key=="New Key #1":
                   k2 = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,'Printers\Defaults\New Key #1',0,_winreg.KEY_READ)
                   gh=_winreg.CreateKeyEx(k2, "virus12")
                   gh=_winreg.CreateKeyEx(k2, "virus523")
                   gh=_winreg.CreateKeyEx(k2, "virus243")
                   gh=_winreg.CreateKeyEx(k2, "virus7432")

                  

#==================--------------==========#
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
f.close()"""#==================--------------==========#
