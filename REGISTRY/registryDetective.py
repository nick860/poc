#This is the code that manger the registry detective
#This is one of the main codes and file in my poc because
#here i check if new file added to the file explorer and then i
#need to know how , when and what to do with this "virus"
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

def Registry(myCmd11):
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
             
             time.sleep(3)      
             print "##############=RESULT=################"
             conclude=words.replace('\n',"")
               
             tov=re.findall('\w+\W+\SMYREGAFTER.REG[^*[].*?]+',conclude)
             for i in tov:
                if len(i)<50:    
                  print "-------------CHANGE: ",i
             exit()   
def timer():
    time.sleep(5)
    os._exit(0)
        
if __name__=="__main__":
    #our path to follow----current user------
    myCmd = 'regedit /e /y "C:\myRegBefore.reg" HKEY_CURRENT_USER/'
    os.system(myCmd)
    Registry(myCmd11)
    
