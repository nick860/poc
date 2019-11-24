import time
import timeit
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler as hand
from watchdog.events import PatternMatchingEventHandler as listen
from threading import Thread as wait
import subprocess

import re

class DetectiveFiles(wait):
    
    def __init__(self,path):
      wait.__init__(self)
      self.my_observer = Observer()
      self.path=path
      
    def run(self):
        my_event_handler = TheEvent()
        self.my_observer.schedule(my_event_handler, self.path, True)#go_recursively
        self.my_observer.start()
        try:
            while True:
                pass
        except:
                self.observer.stop()
        self.observer.join()
            
class TheEvent(hand):
    
    def __init__(self):
        pass
    def on_any_event(self,event):
        if event.is_directory:
             return None
            
        elif event.event_type=="created":
             t0= time.clock()
             print event.event_type,": ",event.src_path
             print "####################################################"
             thefile=re.split(r"\\+",event.src_path)
            
             
             
            
             if event.src_path.find("py")!=-1:
                 y='python '+str(thefile[-1])
                 
                 myCmd11 ="C:\Python27\Scripts\\"+str(thefile[-1])
                 
                 os.system(myCmd11)
                 print "running virus...."
                 time.sleep(3)
             myCmd = 'regedit /e /y "C:\myRegAfter.reg" HKEY_CURRENT_USER/'
             os.system(myCmd)
             print "checking the virus..."
             
             time.sleep(3)
             try:
                 words=subprocess.check_output('fc C:\myRegBefore.reg C:\myRegAfter.reg',shell=True)
             except:
                try:
                 words=subprocess.check_output('fc C:\myRegBefore.reg C:\myRegAfter.reg > results.txt',shell=True)
                except:
                    
                     time.sleep(3)
                     with open(r"C:\Python27\Scripts\results.txt",'r') as input_file:
                       words=input_file.read()
                   
             print "compring between files..."
             t1 = time.clock() - t0
             print("Time elapsed: ", t1 - t0)
             time.sleep(3)      
             print "##############=RESULT=################"
             conclude=words.replace('\n',"")
               
             tov=re.findall('\w+\W+\SMYREGAFTER.REG[^*[].*?]+',conclude)
             for i in tov:
                if len(i)<50:    
                  print "-------------CHANGE: ",i
             exit()   
class RegDetective(wait):
    pass
    #f=os.system('cmd /k "ipconig"')Computer\HKEY_LOCAL_MACHINE\SYSTEM\WPA
    #print f

    
def timer():
    time.sleep(5)
    os._exit(0)
        
if __name__=="__main__":

 
 
    myCmd = 'regedit /e /y "C:\myRegBefore.reg" HKEY_CURRENT_USER/'
    os.system(myCmd)
    
    Files32=DetectiveFiles("C:\Python27\Scripts")
    Reg=RegDetective()
    global filse
    
    #c=threading.Thread(target=timer)
    #c.start()
    
    Files32.start()
    Reg.start()
    
    Files32.join()
    Reg.join()
