import socket                   # Import socket module
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
#The class finds me new file that created in my file explorer
#i did use in moudle that called watchdog

class DetectiveFiles(wait): #wait means that this class working as theard
    
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
#this class finds me which key added or what chaneded in our regisry while
#we have been runing the virus...maybe nothing change
class TheEvent(hand):
    global thefile
    def __init__(self):
        pass
    def on_any_event(self,event):
        global thefile
        if event.is_directory:
             return None
            
        elif event.event_type=="created" and event.src_path.find("poc-poc\OPEN")==-1:
             print event.event_type,": ",event.src_path
             print "####################################################"
             thefile=event.src_path
        else:
            return None
  
port = 60050        # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = "192.168.1.20"     # Get local machine name
s.bind((host,  port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
global thefile
thefile=None
print 'Server listening....'
Files32=DetectiveFiles("C:\Users\Admin\Desktop")
Files32.start()
conn, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
while True:
    
    data = conn.recv(1024)
    print('Server received', repr(data))
    while thefile==None:
        pass
    f = open(thefile,'rb')
    l = f.read(10000)
    conn.send(l)
    print('Sent ',repr(l))
    f.close()
    thefile=None
    print('Done sending')
    
conn.close()
     
