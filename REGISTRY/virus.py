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
