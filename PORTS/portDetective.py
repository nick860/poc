############################ PORTS #############################

#this code is checking the ports
#if the virus is opened some port for listening so i define and discover this
#new connect and kill the procces

import re
import subprocess
import os
import threading
import time
#the virus is running a server which opens new port for clients
def RunTheVirus():
    myCmd11 ="C:\Users\user\Desktop\watchmedo.py"
    os.system(myCmd11)
    time.sleep(4)
#checking before with netstat -ano ...gives me also the pid of port
#i need this to be able to kill process in the end

def CheckBefore():
    global Before,After
    words=subprocess.check_output('netstat -ano',shell=True)
    Before=re.findall('[A-Z]{3}.*?LISTENING+.*?[0-9]+|.*?ESTABLISHED+.*?[0-9]+',words)
    
#for this i check the netstat after the new port created 
def CheckAfter():
    global Before,After
    words=subprocess.check_output('netstat -ano',shell=True)
    After=re.findall('[A-Z]{3}.*?LISTENING+.*?[0-9]+|.*?ESTABLISHED+.*?[0-9]+',words)
    
#here we compring between two lists and see what different
#if there is a new port from our virus we would kill him
def checking():
    global Before,After
    for x in range(0,len(After)-1):
        if Before[x]!=After[x] and After[x].find("10.0.2.15")!=-1:
            print After[x]
            print InBlackList(After[x])
            
            
            
def InBlackList(portDest):
    for x in range (11000,13000):
        if portDest.find(str(x))!=-1:
            return "Danger in port "+ str(x)

if __name__=="__main__":
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
