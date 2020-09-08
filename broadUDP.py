import socket
import time
import sys
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
server.settimeout(0.2)
server.connect(("192.168.10.11", 1235))
pcktsize =  int(raw_input("how big is the packet : ") or "200")
msg = 'X'
message_r = msg*pcktsize
message = message_r.encode()

def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('!I', len(msg)) + msg
    # print(repr(msg))
    sock.sendall(msg)

i=0
for i in range (10000):
    send_msg(server,message)
    i=i+1
    
    sys.stdout.write("No of TX: %d   \r" % (i) )
    sys.stdout.flush()
    time.sleep(0.02)

                                                                                     34,1          All
