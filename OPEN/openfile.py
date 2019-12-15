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
             after=re.findall("MYREGAFTER.REG.*?\*{5}",words)
             try:
               for o in range(15):
                   if len(after[o])>15:
                       print after[o]
             except:
               print "no change in registry"
             exit()



             
def OpenVirus():
   global v
   os.system("virus2.py")
   v=True 
#checks the handle that the process looking on 
def CheckBefore():
   os.system('handle -p python>Before.txt')
   time.sleep(1)

#after the virus did the handle on his files  
def CheckAfter():
   os.system('handle -p python>After.txt')
   time.sleep(3)   

#with to comman line fc (file comper) we can see the differents between
#the two file text --in our case i did filter on python process!
def findOut():    
    time.sleep(1)
    os.system('handle -p python>After.txt')
    time.sleep(3)   
    try: #in our example we need to see changes
      w=subprocess.check_output('fc Before.txt After.txt > results.txt',shell=True)
    except:
        time.sleep(1)    
        with open(r"C:\Users\Admin\Desktop\virus\poc\OPEN\results.txt",'r') as input_file:
              words=input_file.read()
        words=words.replace("\n","")
        before=re.findall("\*+.*?Before.txt.*?AFTER.TXT",words)
        after=re.findall("\*\sAFTER.TXT.*?Befor.txt|\*\sAFTER.TXT.*?\*{5}",words)
        beforefiles=[]
        afterfiles=[]
        
        for files in before:
            listToAdd=re.findall("\w+:.*?C:.*?\s",files)
            beforefiles=beforefiles+listToAdd
        for files in after:
            listToAdd=re.findall("\w+:.*?C:.*?\s",files)
            afterfiles=afterfiles+listToAdd
        save=0 #somtimes we will get None in i
        print afterfiles,beforefiles
        for i in range(len(beforefiles)):
            save=i
            if afterfiles[i]!=beforefiles[i]:
                print "####################################"
                print "The file that opend by another process:  "
                print afterfiles[i]
        save=save+1
        if save==1:
             print "####################################"
             print "The file that opend by another process:  "
        for i2 in range(save,len(afterfiles)-1):
                print i2
                print afterfiles[i2]
        print "####################################"
        return 0
    print "there is no change"
    
if __name__=="__main__":
    
    myCmd = 'regedit /e /y "C:\myRegBefore.reg" HKEY_CURRENT_USER\Printers'
    os.system(myCmd)
    global v
    v=False
    CheckBefore()
    time.sleep(1)
    t0 = threading.Thread(target=Registry, args=["virus.py"])
    t1 = threading.Thread(target=OpenVirus, args=[])
    t2 = threading.Thread(target=CheckAfter, args=[])
    
    t0.start()
    t1.start()
    t2.start()
    time.sleep(1)
    findOut()
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




 
