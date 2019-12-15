import _winreg
f=file(r"C:\Python27\Scripts\new.txt",'w')

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

print "think this is a real virus \n"*77
import time
print " a lot of damge that the virus makes"
time.sleep(4)
