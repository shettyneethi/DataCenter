from __future__ import print_function
import logging

import grpc
import sys
from time import perf_counter 
import lab6_pb2
import lab6_pb2_grpc

def run():
	# NOTE(gRPC Python Team): .close() is possible on a channel and should be
	# used in circumstances in which the with statement does not fit the needs
	# of the code.
	ip = sys.argv[1]
	api = sys.argv[2]
	n = int(sys.argv[3])

	with grpc.insecure_channel(ip+':50051') as channel:
		stub = lab6_pb2_grpc.lab6GRPCStub(channel)
		if api == ( "add" ):
			t1_start = perf_counter()
			for i in range(n):
				response = stub.add(lab6_pb2.addMsg(a=1,b=2))
			t1_stop = perf_counter() 
			print("grpc client received : sum " + str(response.sum))
		elif api == ("image"):
			img = open('Flatirons_Winter_Sunrise_edit_2.jpg', 'rb').read()
			data = lab6_pb2.imageMsg(img=img)
			t1_start = perf_counter()
			for i in range(n):
				response = stub.image(data)
			t1_stop = perf_counter() 
			print("grpc client received: width,height " + str(response.width), str(response.height))
	print("Total Elapsed time during all calls in seconds:",t1_stop-t1_start) 
	print("Elapsed avg time for call in mili-seconds:",(((t1_stop-t1_start)/n)*1000) )

if __name__ == '__main__':
	logging.basicConfig()
	run()