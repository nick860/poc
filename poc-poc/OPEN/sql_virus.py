import sqlite3 as lite
import sys
import datetime
import subprocess
import os
def connect():
    
   
   file_name='C:\\Users\\Admin\\Videos\\virus_db1.db' #the file
   global userid, conn
   conn = None
   err=0
   try:
    conn = lite.connect(file_name)
   except lite.Error, e:
    print "Error %s:" % file_name 
    sys.exit(1)
   finally:
    if conn:
     print "Opened database successfully";
   cursor = conn.cursor()
   userid=0
   return cursor
   
   
def SqliteOrder(hashV, fileName, time):
    
   userid=0
   err=0
   
   cursor=connect()
   #print cursor.execute("delete from users").rowcount
   try:
       for row in cursor.execute('SELECT * FROM users ORDER BY time'):
           userid=userid+1
           
   except:
       pass
       
   print userid    
   if userid==0:
       try: #for the begining table....
        cursor.execute(''' CREATE TABLE users(id INTEGER PRIMARY KEY,
        time  TEXT, fileName TEXT, hashV TEXT) ''')
        cursor.execute('''INSERT INTO users(time, fileName, hashV)
        VALUES(?,?,?)''', (0,0,0)) 
        #cursor.executemany(''' INSERT INTO users(time, fileName, hashV) VALUES(0,0,0)''', users)
        userid=1
       except:
           print userid
           pass

   if userid==10:
       cursor.execute('''UPDATE users SET hashV = ? WHERE id = ? ''',(hashV, userid+1))
       cursor.execute('''UPDATE users SET fileName = ? WHERE id = ? ''',(fileName, userid+1))
       cursor.execute('''UPDATE users SET time = ? WHERE id = ? ''',(time, userid+1))
   else:
       cursor.execute('''INSERT INTO users(time, fileName, hashV)VALUES(?,?,?)''', (time, fileName, hashV))
   conn.commit()

def compering():
    
   userid=0
   err=0
   cursor=connect()
   row_name=[]
   row_hash=[]
   try:
       for row in cursor.execute('SELECT * FROM users ORDER BY time'):
           row_name.append(str(row[2]))
           row_hash.append(str(row[3]))
   except:
       pass
    
   title="ssdeep,1.1--blocksize:hash:hash,filename"
   result1={}
   for i in range(len(row_name)):
       
       with open('hashes.txt', 'w') as f:
           f.write(title+"\n"+str(row_hash[i])+', "virus2.py"')
           
       
       data1=subprocess.check_output('ssdeep -b -m hashes.txt virus2.py',shell=True)
       result=data1[data1.find("(")+1:data1.find(")")]
       result1["The virus "+row_hash[i]]=result
   return result1
                  
   userid=0
   err=0
  
   
   cursor=connect()
     
def add_to_db():
    
    myCmd = 'ssdeep -b virus2.py > hashes.txt'
    os.system(myCmd)
    with open('hashes.txt', 'r') as f:
          tr= f.read()
          tr= tr[tr.find("\n"):]
          hash1= tr[:tr.find(",")]
          name=tr[tr.find(",")+2:-3]

    SqliteOrder(hash1,name, datetime.datetime.now())


#add_to_db()
print compering()
