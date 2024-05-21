import database
from service.proto import getlist_pb2_grpc as getlist_pb2_grpc

class GetListServiceServicer(getlist_pb2_grpc.GetListServiceServicer):
    def GetList(self, request, context):
        response = database.GetList(self, request, context)
        return response