# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from crons.server import planserver_pb2 as planserver__pb2


class PlanStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.set = channel.unary_unary(
        '/planserver.Plan/set',
        request_serializer=planserver__pb2.PlanRequest.SerializeToString,
        response_deserializer=planserver__pb2.PlanReply.FromString,
        )
    self.update = channel.unary_unary(
        '/planserver.Plan/update',
        request_serializer=planserver__pb2.PlanRequest.SerializeToString,
        response_deserializer=planserver__pb2.PlanReply.FromString,
        )
    self.delete = channel.unary_unary(
        '/planserver.Plan/delete',
        request_serializer=planserver__pb2.PlanDelRequest.SerializeToString,
        response_deserializer=planserver__pb2.PlanReply.FromString,
        )
    self.read = channel.unary_unary(
        '/planserver.Plan/read',
        request_serializer=planserver__pb2.PlanDelRequest.SerializeToString,
        response_deserializer=planserver__pb2.PlanReply.FromString,
        )


class PlanServicer(object):
  """The greeting service definition.
  """

  def set(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def update(self, request, context):
    """Sends another greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def read(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PlanServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'set': grpc.unary_unary_rpc_method_handler(
          servicer.set,
          request_deserializer=planserver__pb2.PlanRequest.FromString,
          response_serializer=planserver__pb2.PlanReply.SerializeToString,
      ),
      'update': grpc.unary_unary_rpc_method_handler(
          servicer.update,
          request_deserializer=planserver__pb2.PlanRequest.FromString,
          response_serializer=planserver__pb2.PlanReply.SerializeToString,
      ),
      'delete': grpc.unary_unary_rpc_method_handler(
          servicer.delete,
          request_deserializer=planserver__pb2.PlanDelRequest.FromString,
          response_serializer=planserver__pb2.PlanReply.SerializeToString,
      ),
      'read': grpc.unary_unary_rpc_method_handler(
          servicer.read,
          request_deserializer=planserver__pb2.PlanDelRequest.FromString,
          response_serializer=planserver__pb2.PlanReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'planserver.Plan', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
