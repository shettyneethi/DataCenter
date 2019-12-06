from concurrent import futures
import logging
from PIL import Image
import grpc
import io
import lab6_pb2
import lab6_pb2_grpc


class lab6GRPC(lab6_pb2_grpc.lab6GRPCServicer):

    def add(self, request, context):
        return lab6_pb2.addReply(sum=int(request.a+request.b))

    def image(self, request, context):
    	# convert the data to a PIL image type so we can extract dimensions
    	ioBuffer = io.BytesIO(request.img)
    	img = Image.open(ioBuffer)
    	# build a response dict to send back to client
    	return lab6_pb2.imageReply(width = img.size[0], height = img.size[1])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lab6_pb2_grpc.add_lab6GRPCServicer_to_server(lab6GRPC(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()