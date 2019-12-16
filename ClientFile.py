import socket                   # Import socket module
import os
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60008                   # Reserve a port for your service.

s.connect((host, port))
s.send("Hello server!")

with open('C:\Users\Admin\Desktop\uuseme.py', 'w') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)
        myCmd='uuseme.py'
        os.system(myCmd)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')
