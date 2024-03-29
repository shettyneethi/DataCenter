# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import lab6_pb2 as lab6__pb2


class lab6GRPCStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.add = channel.unary_unary(
        '/lab6.lab6GRPC/add',
        request_serializer=lab6__pb2.addMsg.SerializeToString,
        response_deserializer=lab6__pb2.addReply.FromString,
        )
    self.image = channel.unary_unary(
        '/lab6.lab6GRPC/image',
        request_serializer=lab6__pb2.imageMsg.SerializeToString,
        response_deserializer=lab6__pb2.imageReply.FromString,
        )


class lab6GRPCServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def add(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def image(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_lab6GRPCServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'add': grpc.unary_unary_rpc_method_handler(
          servicer.add,
          request_deserializer=lab6__pb2.addMsg.FromString,
          response_serializer=lab6__pb2.addReply.SerializeToString,
      ),
      'image': grpc.unary_unary_rpc_method_handler(
          servicer.image,
          request_deserializer=lab6__pb2.imageMsg.FromString,
          response_serializer=lab6__pb2.imageReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'lab6.lab6GRPC', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
