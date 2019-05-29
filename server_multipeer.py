import socket
import sys
import time
import os

import termios
import tty
import thread

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
#client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(('', 50002))
#client.bind(("127.0.0.1",1236))

class new_client:

	def __init__(self, whichID, packet):
		self.ID = whichID

		self.i=0
		#past_p = time.time()
   		self.IAT = 0.0
   		self.sumIAT = 0.0
		self.freq = 0.0

		self.past_p = 0.0
		self.datasize = 0.0



	def analyze(self,packet):
		if (packet[:1]==self.ID):
			if not (self.i==0):
   				time_p = time.time() - self.past_p
   				self.sumIAT += time_p
   				self.IAT=self.sumIAT/self.i
				self.freq=1.0/self.IAT

			self.datasize = len(packet)
			self.i=self.i+1
			self.past_p = time.time()

		sys.stdout.write("ID: %s; No of RX: %d packets; IAT: %0.6f sec; Freq: %0.2f; %d bytes Through: %0.3f Mbit/s\n" % (self.ID, self.i, self.IAT, self.freq , self.datasize ,self.freq*self.datasize*8/1000000))


IDList = []
Client = []

pcktsize =  int(raw_input("how big is the packet : ") or "200")
i=0

while True:


   data = client.recv(pcktsize)

   if not data: break

   id = data[:1]

   if id not in IDList:
	IDList.append(id)
   	Client.append(new_client(id,data))

   for x in range (len(Client)):
	Client[x].analyze(data)

   sys.stdout.write("No of Clients %d" % len(Client))
   for _ in range(len(Client)):
   	sys.stdout.write("\033[F")
   sys.stdout.flush()

print(sumIAT/i)
client.close()
