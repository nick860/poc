#this program caches an process(our virus) that opens some other file
#if the virus opens another file we will print the changes and which file has been
#opened


import subprocess
import time
import os
import re
import threading

#run the virus ...in our case (just for the example) open and tries to open
#file
def OpenVirus():
  subprocess.check_output('cd C:\porc',shell=True)
  os.system("virus2.py")

#checks the handle that the process looking on 
def CheckBefore():
   subprocess.check_output('handle -p python>Before.txt',shell=True)
   time.sleep(1)

#after the virus did the handle on his files  
def CheckAfter():
   subprocess.check_output('handle -p python>After.txt',shell=True)
   time.sleep(3)   

#with to comman line fc (file comper) we can see the differents between
#the two file text --in our case i did filter on python process!
def findOut():    
    time.sleep(1)
    subprocess.check_output('handle -p python>After.txt',shell=True)
    time.sleep(3)   
    try: #in our example we need to see changes
      w=subprocess.check_output('fc Before.txt After.txt > results.txt',shell=True)
    except:
        time.sleep(1)    
        with open(r"C:\porc\results.txt",'r') as input_file:
              words=input_file.read()
        words=words.replace("\n","")
        before=re.findall("\*+.*?Before.txt.*?AFTER.TXT",words)
        after=re.findall("\*\sAFTER.TXT.*?Befor.txt|\*\sAFTER.TXT.*?\*{5}",words)
        beforefiles=[]
        afterfiles=[]
        print afterfiles,beforefiles
        for files in before:
            listToAdd=re.findall("\w+:.*?C:.*?\s",files)
            beforefiles=beforefiles+listToAdd
        for files in after:
            listToAdd=re.findall("\w+:.*?C:.*?\s",files)
            afterfiles=afterfiles+listToAdd
        save=0 #somtimes we will get None in i
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
    os.chdir("C:\porc")
    
    CheckBefore()
    time.sleep(1)
    t1 = threading.Thread(target=OpenVirus, args=[])
    t2 = threading.Thread(target=CheckAfter, args=[])
    
    t1.start()
    t2.start()
    time.sleep(1)
    findOut()




 
