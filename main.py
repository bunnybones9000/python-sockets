import socket
import sys

try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as err:
    print("failed to create socket")
    print("reason:"+str(err))
print ("socket created")

target_host = input("enter the target host name to connect: ")
target_port = input ("enter the target port to connect: ")
try:
    sock.connect((target_host, int(target_port)))
    print(f"socket connected to {target_host} on port {target_port} ")
    sock.shutdown(2)
except socket.error as err :
    print(f"failed to connect to {target_host} on {target_port}")
    print("reason:"+ str(err))
    sys.exit()