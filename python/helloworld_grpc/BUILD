
py_binary(
    name = "server",
    srcs = ["server.py"],
    deps = [
        "//grpc_def/helloworld:helloworld_py_pb2",
        "//grpc_def/helloworld:helloworld_py_pb2_grpc",
    ],
)

py_binary(
    name = "client",
    srcs = ["client.py"],
    deps = [
        "//grpc_def/helloworld:helloworld_py_pb2",
        "//grpc_def/helloworld:helloworld_py_pb2_grpc",
    ],
)

# This tests uses and a shell based target to run the binary targets above.
# Note that this invokes and additional compile step for its data dependencies,
# and thus a large part of the source in this repository. That's not ideal since
# it takes almost twice as long. It is nevertheless includes here to demonstrate
# that it can be done. But it doesn't mean that you should.
sh_test(
    name = "test",
    srcs = ["test.sh"],
    data = [
        ":server",
	":client",
    ],
)
