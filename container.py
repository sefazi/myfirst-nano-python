from concurrent import futures
import grpc
from service.proto import getlist_pb2 as getlist_pb2
from service.proto import getlist_pb2_grpc as getlist_pb2_grpc
import time
import methods

class GRPCServerContainer:
    def __init__(self, host='[::]', port=8081, max_workers=10):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
        getlist_pb2_grpc.add_GetListServiceServicer_to_server(
            methods.GetListServiceServicer(),
            self.server)
        self.server.add_insecure_port(f'{host}:{port}')

    def start(self):
        self.server.start()
        print(f"Server started, listening on port 8081.")
        try:
            while True:
                time.sleep(86400)  # Keep the server running
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self.server.stop(0)
        print("Server stopped.")