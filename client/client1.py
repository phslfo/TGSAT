import socket

HOST = 'localhost'    # The remote host
PORT = 7001           # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall('Finn is a ugly guy.')
data = s.recv(1024)
s.close()

print 'Received', repr(data)