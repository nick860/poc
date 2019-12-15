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
             time.sleep(6)
             myCmd = 'regedit /e /y "C:\myRegAfter.reg" HKEY_CURRENT_USER\Printers'
             os.system(myCmd)
             print "checking the virus..."
             os.system('fc C:\myRegBefore.reg C:\myRegAfter.reg > result.txt')
             print "compring between files..."
             with open(r"C:\Users\Admin\Desktop\virus\poc\REGISTRY\result.txt",'r') as input_file:
                       words=input_file.read()
             time.sleep(3)
             words=words.replace("\n","")
             after=re.findall("MYREGAFTER.REG.*?\*{5}",words)
             for o in range(15):
                 if len(after[o])>15:
                     print after[o]           
             exit()  
if __name__=="__main__":

    myCmd = 'regedit /e /y "C:\myRegBefore.reg" HKEY_CURRENT_USER\Printers'
    os.system(myCmd)
    Registry("virus.py")
   
