import socket

HOST = 'localhost'    # The remote host
PORT = 7002           # The same port as used by the server

#teste = ['ugly', 'horrible', 'beautiful ugly', 'awesome', ' ']
#teste = ['If #Santorum becomes the republican candidate for the #uselection the republican party will lose']
problema = '@faithsone u so smart & progressive. i thought u were like @moontoseu or rick santorum ^^'
#teste = problema.split()
teste = [problema]
#teste = ['racist']

for i in teste:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    s.sendall(str(i))
    data = s.recv(1024)
    
    print str(i), repr(data)

    s.close()
