import socket                   # Import socket module
import os
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60020                  # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")


while True: 
    print('receiving data...')
    data = s.recv(10000)
    print('data=%s', (data))
    if not data:
           break
     # write data to a file
    with open('C:\Users\Admin\Desktop\uusemee.py', 'w') as f:
      print 'file opened'
      f.write(data)
    s.send("Hello server!")

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
