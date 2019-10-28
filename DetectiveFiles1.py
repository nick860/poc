import time
import win32file
import threading
import win32api
import win32event
import win32con
import _winreg
import os
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler as hand
from watchdog.events import PatternMatchingEventHandler as listen
from threading import Thread as wait

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
                time.sleep(1)
        except:
                self.observer.stop()
        self.observer.join()
            
class TheEvent(hand):
    
    def __init__(self):
        pass
    def on_any_event(self,event):
        if event.is_directory:
             return None
            
        elif event.event_type:         
             print event.event_type

class RegDetective(wait):
    
    def __init__(self):
        wait.__init__(self)
        self.key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,'SYSTEM',0,_winreg.KEY_READ)
        
    def run(self):
        evt=self.runNoMain(self.key)
        while 1:
            time.sleep(1)
            ret_code=win32event.WaitForSingleObject(evt,500)#Returns when an event is signalled
            if ret_code == win32con.WAIT_OBJECT_0:
                print "Changed in Registry !!"
                evt=self.runNoMain(self.key)
            if ret_code == win32con.WAIT_TIMEOUT:
                 pass
                
    def runNoMain(self,key):
        evt = win32event.CreateEvent(None,0,0,None)#PyHANDLE-Creates a waitable event
        #Notifies the caller about changes to the attributes or contents of a specified registry key.
        win32api.RegNotifyChangeKeyValue(self.key #A handle to an open registry key
                                         , 1,
                                         
        win32api.REG_NOTIFY_CHANGE_NAME |
        win32api.REG_NOTIFY_CHANGE_ATTRIBUTES |
        win32api.REG_NOTIFY_CHANGE_LAST_SET |
        win32api.REG_NOTIFY_CHANGE_SECURITY                                

        , evt #A handle to an event
        , True)
        
        return evt
    
def timer():
    time.sleep(5)
    os._exit(0)
        
if __name__=="__main__":
    
    Files32=DetectiveFiles("C:\Python27\Scripts")
    Reg=RegDetective()
    
    #c=threading.Thread(target=timer)
    #c.start()
    
    Files32.start()
    Reg.start()
    #os.system('python filename.py')
    Files32.join()
    Reg.join()    
    
