import socket
from analisador import Classificador   

HOST = 'localhost'
PORT = 7002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

cl = Classificador(False, False, False, True)

print 'Analisador 2 inicializado na porta', PORT

while 1:
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data: continue
    
    result = cl.analisar(data)
    
    conn.sendall(str(result))
    conn.close()
