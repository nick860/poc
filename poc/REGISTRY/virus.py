<<<<<<< HEAD:poc-poc/OPEN/virus2.py.py
import _winreg
from socket import *
f=file(r"C:\Python27\Scripts\new2.txt",'w')
f2=file(r"C:\Python27\Scripts\new1.txt",'w')
f3=file(r"C:\Python27\Scripts\new3.txt",'w')
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
                  
host='192.168.1.20'
port=11248
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

=======
import _winreg

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
                  
        
print "ddddddd"
>>>>>>> f07fbe483e985bb0e2101f38c08ae398cf98fa59:poc/REGISTRY/virus.py
