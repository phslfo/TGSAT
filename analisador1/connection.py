import socket
import analisador

HOST = 'localhost'
PORT = 7001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print 'Analisador 1 inicializado na porta', PORT

while 1:
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data: continue
    
    result = analisador.sentiment(data)
    
    conn.sendall(str(result))
    conn.close()
