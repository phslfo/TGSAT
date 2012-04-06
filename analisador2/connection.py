import socket
import analisador

HOST = 'localhost'
PORT = 7002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

cl = analisador.Classificador()

while 1:
    print 'aqui'
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data: continue
    
    result = cl.analisar(data)
    
    conn.sendall(str(result))
    conn.close()
