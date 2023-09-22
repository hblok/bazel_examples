#!/usr/bin/python3

from concurrent import futures

import grpc

from grpc_def.helloworld import helloworld_pb2
from grpc_def.helloworld import helloworld_pb2_grpc


class Server(helloworld_pb2_grpc.GreeterServicer):
    
    def start(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        helloworld_pb2_grpc.add_GreeterServicer_to_server(self, server)
        server.add_insecure_port("[::]:50051")
        server.start()
        server.wait_for_termination()
    
    def SayHello(self, request, context):
        print("On server: Hello from %s" % request.name)
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)


if __name__ == "__main__":
    server = Server()
    server.start()
