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
from beautifultable import BeautifulTable
import subprocess
import pickle
import re
import sql_virus as sql

#The class finds me new file that created in my file explorer
#i did use in moudle that called watchdog


def putInTable(table,i, name,arr):
    for x in range(i):
        table[x][name]=arr[x]
        
def printResult(Reg, Han, Port):
    table = BeautifulTable()
    table.column_headers = ["Change No.","Registry changes", "Files in use", "Ports connection"]
    lent=max(len(Reg),len(Han),len(Port))

    for i in range(lent):
             table.append_row(["No."+str(i+1), "", "",""])

    makeName=["Registry changes","Files in use","Ports connection"]
    arrs=[Reg,Han,Port]
    for x in range(3):
       putInTable(table,len(arrs[x]),makeName[x],arrs[x])
        
    print len(str(table))                        
    print table
    
  
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
            
        elif event.event_type=="created":
             thefile.append(event.src_path)
             
  
port = 60077       # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = "172.16.12.177"     # Get local machine name
s.bind((host,  port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.
global thefile
thefile=[]
print 'Server listening....'
Files32=DetectiveFiles("C:\Users\u101040.DESHALIT\Pictures")
Files32.start()

 
conn, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
while True:
    data = conn.recv(1024)
    try:
        my_list= pickle.loads(data)
        if len(my_list)>0:
            sql.add_to_db()
        try:
            Reg=my_list[0]
            Han=my_list[1]
            Port=my_list[2]
            
            printResult(Reg,Han,Port)

        except:
            raise
    except:
        pass
    while len(thefile)==0:
        pass

    
    f = open(thefile[-1],'rb')
    txt=f.read()
    with open("virus2.py","w") as f2:
        f2.write(txt)
        
    result=""
    """arr=sql.compering()
    print arr
    for i in arr:        
        if i[1].find("(")!=-1:
           y= i[1][i[1].find("(")+1:i[1].find(")")]
           print y+";"
           try:
              if int(y)>70:
                  result="virus"
           except:
              pass"""
 
            
    print "scanning : " , thefile[-1]
    if result=="virus":
        thefile=thefile[:-1]
        print "the file is already virus"
        pass
    else:
        l = f.read(10000)
        conn.send(l) 
        f.close()
        thefile=thefile[:-1]
        print('Done sending')
    
conn.close()
     
