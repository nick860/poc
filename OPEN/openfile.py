#this program caches an process(our virus) that opens some other file
#if the virus opens another file we will print the changes and which file has been
#opened
import subprocess
import time
import os
import re
import threading
import sys
#run the virus ...in our case (just for the example) open and tries to open
#file
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
    for x in range(0,len(Before)-1):
        if Before[x]!=After[x] and After[x][31:].find('192.168.1.20')!=-1:
            print After[x]
            print InBlackList(After[x][31:])
            
    for x in range(len(Before)-1,len(After)-1):
        
        if After[x][31:].find('192.168.1.20')!=-1:
            print After[x]
            print InBlackList(After[x][31:])
            
def InBlackList(portDest):
    for x in range (11000,13000):
        if portDest.find(str(x))!=-1:
            return "Danger in port "+ str(x)


def Registry(myCmd11):
             global v
             while v==False:
               pass
             print "running virus...."
             time.sleep(6)
             myCmd = 'regedit /e /y "C:\myRegAfter.reg" HKEY_CURRENT_USER\Printers'
             os.system(myCmd)
             print "checking the virus..."
             os.system('fc C:\myRegBefore.reg C:\myRegAfter.reg > result.txt')
             print "compring between files..."
             with open(r"C:\Users\Admin\Desktop\virus\poc\OPEN\result.txt",'r') as input_file:
                       words=input_file.read()
             time.sleep(3)
             words=words.replace("\n","")
             AfterH=re.findall("MYREGAFTER.REG.*?\*{5}",words)
             try:
               for o in range(15):
                   if len(AfterH[o])>15:
                       print AfterH[o]
             except:
               print "no change in registry"
             exit()



             
def OpenVirus():
   global v
   os.system("virus2.py")
   v=True 
#checks the handle that the process looking on 
def CheckBeforeHandle():
   os.system('handle -p python>BeforeH.txt')
   time.sleep(1)

#AfterH the virus did the handle on his files  
def CheckAfterHandle():
   os.system('handle -p python>AfterH.txt')
   time.sleep(3)   

#with to comman line fc (file comper) we can see the differents between
#the two file text --in our case i did filter on python process!
def findOut():    
    time.sleep(1)
    os.system('handle -p python>AfterH.txt')
    time.sleep(3)   
    try: #in our example we need to see changes
      w=subprocess.check_output('fc BeforeH.txt AfterH.txt > results.txt',shell=True)
    except:
        time.sleep(1)    
        with open(r"C:\Users\Admin\Desktop\virus\poc\OPEN\results.txt",'r') as input_file:
              words=input_file.read()
        words=words.replace("\n","")
        BeforeH=re.findall("\*+.*?BeforeH.txt.*?AfterH.TXT",words)
        AfterH=re.findall("\*\sAFTER.TXT.*?Befor.txt|\*\sAFTER.TXT.*?\*{5}",words)
        beforefiles=[]
        afterfiles=[]
        
        for files in BeforeH:
            listToAdd=re.findall("\w+:.*?C:.*?\s",files)
            beforefiles=beforefiles+listToAdd
        for files in AfterH:
            listToAdd=re.findall("\w+:.*?C:.*?\s",files)
            afterfiles=afterfiles+listToAdd
        save=0 #somtimes we will get None in i
    
        i=0
        for i in range(len(beforefiles)):
            if afterfiles[i]!=beforefiles[i] and afterfiles[i].find(" C:\Python27\Scripts")!=-1:
                print "####################################"
                print "The file that opend by another process:  "
                print afterfiles[i]
        for i in range(len(beforefiles),len(afterfiles)):
                if afterfiles[i].find(" C:\Python27\Scripts")!=-1:
                  print afterfiles[i]
    print "there is no change"
    
if __name__=="__main__":
    
    #myCmd = 'regedit /e /y "C:\myRegBefore.reg" HKEY_CURRENT_USER\Printers'
    #os.system(myCmd)
    #global v
    #v=False
    global Before,After
    Before=[]
    After=[]
    #global BeforeH,AfterH
    #BeforeH=[]
   # AfterH=[]
    CheckBefore()
    #CheckBeforeHandle()
    #time.sleep(1)
    #t0 = threading.Thread(target=Registry, args=["virus.py"])
    #t1 = threading.Thread(target=OpenVirus, args=[])
    """t2 = threading.Thread(target=CheckAfterHandle, args=[])
    t3 = threading.Thread(target=CheckAfter, args=[])
    t4 = threading.Thread(target=checking, args=[])
    
    
    t1.start()
    t3.start()
    time.sleep(2)
    t4.start()
    #t2.start()
   
    #t0.start()
    """
    t1 = threading.Thread(target=OpenVirus, args=[])
    t1.start()
    time.sleep(1)
    
    t2 = threading.Thread(target=CheckAfter, args=[])
    t2.start()
    time.sleep(1)

    t3 = threading.Thread(target=checking(), args=[])
    t3.start()
    print "no change"
    
    """global reg, v
    v=False
    reg=False
    #t0 = threading.Thread(target=Registry, args=["virus.py"])
    CheckBefore()
    time.sleep(1)
    
    t2 = threading.Thread(target=CheckAfter, args=[])
    #t0.start()
    OpenVirus()
    time.sleep(2)
    t2.start()
    time.sleep(1)
    findOut()"""




 
