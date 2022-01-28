#
# https://stackoverflow.com/questions/21089268/python-service-discovery-advertise-a-service-across-a-local-network
#
from socket import socket, AF_INET, SOCK_DGRAM

PORT = 50000
MAGIC = bytes('xu49d",'utf-8')

s = socket(AF_INET, SOCK_DGRAM) #create UDP socket
s.bind(('', PORT))

while 1:
    data, addr = s.recvfrom(1024) #wait for a packet
    if data.startswith(MAGIC):
        print("got service announcement from", data[len(MAGIC):])
              
