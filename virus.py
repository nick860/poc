import _winreg

k = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,'SYSTEM',0,_winreg.KEY_READ)
info = _winreg.QueryInfoKey(k)
for i in range(info[0]):
               key = _winreg.EnumKey(k,i)
               print 
               if key=="WPA":
                   k2 = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,'SYSTEM\WPA',0,_winreg.KEY_READ)
                   
                   gh=_winreg.CreateKeyEx(k2, "virus")

        
