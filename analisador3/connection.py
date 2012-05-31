import socket
from sentiment import Classifier

HOST = 'localhost'
PORT = 7003

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

cl = Classifier()

print 'Analisador 3 inicializado na porta', PORT

while 1:
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data: continue
    
    result = cl.analisar(data)
    
    conn.sendall(str(result))
    conn.close()
