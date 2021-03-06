# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import models.text_match_v1.protos.faiss_server_pb2 as faiss__server__pb2


class FaissServerStub(object):
  """interface
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.search = channel.unary_unary(
        '/faiss_server.FaissServer/search',
        request_serializer=faiss__server__pb2.SearchRequest.SerializeToString,
        response_deserializer=faiss__server__pb2.SearchReply.FromString,
        )
    self.add = channel.unary_unary(
        '/faiss_server.FaissServer/add',
        request_serializer=faiss__server__pb2.AddRequest.SerializeToString,
        response_deserializer=faiss__server__pb2.AddReply.FromString,
        )
    self.get_count = channel.unary_unary(
        '/faiss_server.FaissServer/get_count',
        request_serializer=faiss__server__pb2.GetCountRequest.SerializeToString,
        response_deserializer=faiss__server__pb2.GetCountReply.FromString,
        )


class FaissServerServicer(object):
  """interface
  """

  def search(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def add(self, request, context):
    """rpc search_many (SearchManyRequest) returns (SearchManyReply) {} 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get_count(self, request, context):
    """rpc get_index (GetIndexRequest) returns (GetIndexReply) {} 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FaissServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'search': grpc.unary_unary_rpc_method_handler(
          servicer.search,
          request_deserializer=faiss__server__pb2.SearchRequest.FromString,
          response_serializer=faiss__server__pb2.SearchReply.SerializeToString,
      ),
      'add': grpc.unary_unary_rpc_method_handler(
          servicer.add,
          request_deserializer=faiss__server__pb2.AddRequest.FromString,
          response_serializer=faiss__server__pb2.AddReply.SerializeToString,
      ),
      'get_count': grpc.unary_unary_rpc_method_handler(
          servicer.get_count,
          request_deserializer=faiss__server__pb2.GetCountRequest.FromString,
          response_serializer=faiss__server__pb2.GetCountReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'faiss_server.FaissServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
