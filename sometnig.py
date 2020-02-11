#this program caches an process(our virus) that opens some other file
#if the virus opens another file we will print the changes and which file has been
#opened
try:
    import subprocess
    import time
    import os
    import re
    import threading
    import sys
    import socket                   # Import socket module
    global ready
    from beautifultable import BeautifulTable
    mutex = threading.Semaphore(1)
    
    def putInTable(table,i, name,arr):
        for x in range(i):
            table[x][name]=arr[x]
    def printResult():
        global Reg, Han, Port, s
        table = BeautifulTable()
        table.column_headers = ["Change No.","Registry changes", "Files in use", "Ports connection"]
        lent=max(len(Reg),len(Han),len(Port))

        for i in range(lent):
                table.append_row(["No."+str(i+1), "", "",""])

        makeName=["Registry changes","Files in use","Ports connection"]
        arrs=[Reg,Han,Port]
        for x in range(3):
            putInTable(table,len(arrs[x]),makeName[x],arrs[x])
                                 
            
    #run the virus ...in our case (just for the example) open and tries to open
    #file
    def CheckBefore():
        global Before,After
        os.system('netstat -ano > befe.txt')
        with open(r"befe.txt",'r') as input_file:
                           words=input_file.read()
        Before=re.findall('[A-Z]{3}.*?LISTENING+.*?[0-9]+|.*?ESTABLISHED+.*?[0-9]+',words)

    #for this i check the netstat after the new port created 
    def CheckAfter():
        global Before,After
        mutex.acquire()
        os.system('netstat -ano > afae.txt')
        mutex.release()
        with open(r"afae.txt",'r') as input_file:
                           words=input_file.read()
        After=re.findall('[A-Z]{3}.*?LISTENING+.*?[0-9]+|.*?ESTABLISHED+.*?[0-9]+',words)
        checking()
    #here we compring between two lists and see what different
    #if there is a new port from our virus we would kill him
    def checking():
        global Before,After, Port
        for x in range(0,len(Before)-1):
            if Before[x]!=After[x] and After[x][29:].find('192.168.1.20')!=-1:
                if InBlackList(After[x][31:])!="no":
                    Port.append(InBlackList(After[x][29:]))
                    mydata= After[x][-8:]
                      
        for x in range(len(Before)-1,len(After)-1):       
            if After[x][31:].find('192.168.1.20')!=-1 and InBlackList(After[x][31:])!="no":
                Port.append(InBlackList(After[x][31:]))
                
    def InBlackList(portDest):
        for x in range (11000,14000):
            if portDest.find(str(x))!=-1:
                return str(x)
        return "no"
    def Registry():
            global Reg
            myCmd = 'regedit /e /y "C:\myRegAfter.reg" HKEY_CURRENT_USER\Printers'
            mutex.acquire()
            time.sleep(2)
            os.system(myCmd)
            time.sleep(2)
            os.system('fc C:\myRegBefore.reg C:\myRegAfter.reg > result.txt')
            mutex.release()
            with open(r"result.txt",'r') as input_file:
                    words=input_file.read()
                    #print words
            if words.find("no differences encountered")!=-1:
                    print "no differences encountered in registry"
                    return 0
            words=words.replace("\n","")
            AfterH=re.findall("MYREGAFTER.REG.*?\*{5}",words)
            try:
              for o in range(15):
                if len(AfterH[o])>15:
                    Reg.append(AfterH[o])
            except:
              pass
                                
    def OpenVirus():
       global ready,v
       while ready==False:
           pass
       print "=============================RUNNING==========================="
       os.system("virus2.py")
       v=True 
    #checks the handle that the process looking on 
    def CheckBeforeHandle():
        
       os.system('handle -p python>BeforeH.txt')

    #AfterH the virus did the handle on his files  
    def CheckAfterHandle():
       mutex.acquire() 
       os.system('handle -p python>AfterH.txt')
       mutex.release()
       findOut()   

    #with to comman line fc (file comper) we can see the differents between
    #the two file text --in our case i did filter on python process!
    def findOut():
        global Han
        mutex.acquire()
        os.system('fc BeforeH.txt AfterH.txt > results.txt')
        mutex.release()
        try:      
            with open(r"results.txt",'r') as input_file:
                  words=input_file.read()
            words=words.replace("\n","")
          
            while 1:
                if words.find("C:\Python27\Scripts")!=-1:
                   words= words[words.find("C:\Python27\Scripts"):]
                   save=words[:words.find(" ")]
                   Han.append(save)
                   words=words[words.find(" "):]
                else:
                    break
        except:
            raise        
    def connctionToServer():
        global ready, table
        ready=False
        s = socket.socket()             # Create a socket object
        host = "192.168.1.20"     # Get local machine name
        port = 60077              # Reserve a port for your service.

        s.connect((host, port))
        s.send("Hello server!")
        while True:
            time.sleep(2)

            ready=False
            data = s.recv(10000)
                
            if not data:
                   breaks
             # write data to a file
            with open('virus2.py', 'w') as f:
                 
                  f.write(data)
                  ready=True

            while table==None:
                pass
            while len(table)<30:
                pass
            s.send("yes its")
            
        f.close()
        s.close()        
    def Test():
        global Reg, Han, Port, ready
        t0 = threading.Thread(target=connctionToServer, args=[]).start()  
        t1 = threading.Thread(target=OpenVirus, args=[]).start()
        
        while ready==False:
               pass
            
        t2 = threading.Thread(target=Registry, args=[]).start()    
        time.sleep(3)
        start = time.clock()
       
        time.sleep(3)
        CheckAfterHandle()       
        t3 = threading.Thread(target=CheckAfter, args=[]).start()
        time.sleep(3)
        t4 = threading.Thread(target=findOut, args=[]).start()
       
        time.sleep(3)
        end = time.clock()
        print end - start
        printResult()                    
    if __name__=="__main__":
        
        myCmd = 'regedit /e /y "C:\myRegBefore.reg" HKEY_CURRENT_USER\Printers'
        os.system(myCmd)
        global Reg, Han, Port, table
        table=None
        Reg=[]
        Han=[]
        Port=[]
        
        CheckBeforeHandle()
        CheckBefore()
        global Before,After,ready
        ready=False
        Before=[]
        After=[]
        Test()
        time.sleep(3)
        
        global BeforeH,AfterH
        BeforeH=[]
        AfterH=[]  

except:
    raise


