import socket                   # Import socket module
import os
global ready
import time
ready=False

s = socket.socket()             # Create a socket object
host = "192.168.1.20"     # Get local machine name
port = 60032                  # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")


while True:
    time.sleep(2)
    print('receiving data...')
    ready=False
    data = s.recv(10000)
    print('data=%s', (data))    
    if not data:
           break
     # write data to a file
    with open('C:\Users\user\Desktop\poc-poc\OPEN\virus2', 'w') as f:
      print 'file opened'
      f.write(data)
      ready=True
    s.send("Hello server!")

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
