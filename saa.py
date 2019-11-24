import re
import subprocess
import os
import threading
import time
def RunTheVirus():
    myCmd11 ="C:\Users\Admin\Pictures\serverNick.py"
    os.system(myCmd11)

def CheckBefore():
    global Before,After
    words=subprocess.check_output('netstat -ano',shell=True)
    Before=re.findall('[A-Z]{3}.*?LISTENING+.*?[0-9]+|.*?ESTABLISHED+.*?[0-9]+',words)
    

def CheckAfter():
    global Before,After
    words=subprocess.check_output('netstat -ano',shell=True)
    After=re.findall('[A-Z]{3}.*?LISTENING+.*?[0-9]+|.*?ESTABLISHED+.*?[0-9]+',words)
    

def checking():
    global Before,After
    for x in range(0,len(After)-1):
        if Before[x]!=After[x]:
            print After[x]
            mydata= After[x][-8:]
            
            portKill=re.findall("[0-9]+",mydata)
            print portKill
            words=subprocess.check_output('taskkill /PID '+portKill[0]+" /F",shell=True)
            print "Killed the new port successfuly!"
            break


global Before,After
Before=[]
After=[]
CheckBefore()
time.sleep(1)
t1 = threading.Thread(target=RunTheVirus, args=[])
t1.start()
time.sleep(1)

t2 = threading.Thread(target=CheckAfter, args=[])
t2.start()
time.sleep(1)

t3 = threading.Thread(target=checking(), args=[])
t3.start()

print "no change"
