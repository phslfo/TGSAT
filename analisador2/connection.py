import socket
from analisador_modificado import Classificador

HOST = 'localhost'
PORT = 7002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

cl = Classificador(train1=True, train2=False, test=(0,0), train=(0,1000))

print 'Analisador 2 inicializado na porta', PORT

while 1:
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data: continue
    
    result = cl.analisar(data)
    
    conn.sendall(str(result))
    conn.close()
