#!/usr/bin/python3

import grpc
from grpc_def.helloworld import helloworld_pb2
from grpc_def.helloworld import helloworld_pb2_grpc


class Client:

    def start(self):
        channel = grpc.insecure_channel("localhost:50051")
        self.stub = helloworld_pb2_grpc.GreeterStub(channel)

        print("\n" * 3)

    def hello(self):
        response = self.stub.SayHello(helloworld_pb2.HelloRequest(name="Bob"))
        print("Greeter client received from server: " + response.message)


if __name__ == '__main__':
    client = Client()
    client.start()
    client.hello()
