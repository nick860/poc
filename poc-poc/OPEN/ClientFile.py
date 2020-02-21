import socket                   # Import socket module
import os
global ready
s = socket.socket()             # Create a socket object
host = "192.168.1.20"     # Get local machine name
port = 60028                 # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")
ready=Fals

while True:
    ready=False
    print('receiving data...')
    data = s.recv(10000)
    if not data:
           break
     # write data to a file
    with open('virus2.py', 'w') as f:
      f.write(data)
      ready=True
      
    s.send("Hello server!")
    
f.close()
print('Successfully get the file')
s.close()
print('connection closed')
