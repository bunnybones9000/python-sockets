import socket
import sys

my_ip = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((my_ip, 8080))
server.listen(5)

while True:
    print("server waiting for connections")
    client,addr =server.accept()
    print("client connected from ",addr)
    while True:
        data = client.recv(1024)
        if not data or data.decode('utf-8') == 'END':
            break
        print("received from client client : %s"%data.decode('utf-8'))
        try:
            client.send(bytes('hey client','utf-8'))
        except:
            print("exited by user")
    client.close()         
server.close()     