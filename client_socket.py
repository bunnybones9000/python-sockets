import socket
import sys 

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_ip = (socket.gethostbyname(socket.gethostname()))

client.connect((my_ip,8080))

pay_load = 'hey server'

try:
    while True:
        client.send(pay_load.encode('utf-8'))
        data = client.recv(1024)
        print(str(data))
        more = input("do you want to send some thing to the server")
        if more.lower() == 'y':
            pay_load = input("enter payload")
        else:
            break
except KeyboardInterrupt:
    print("exited by user")
client.close()    