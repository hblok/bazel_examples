# Inspired by the GRPC Hello world example at
#
# https://github.com/grpc/grpc/blob/v1.43.0/examples/protos/BUILD


load("@rules_proto//proto:defs.bzl", "proto_library")
#load("@com_github_grpc_grpc//bazel:cc_grpc_library.bzl", "cc_grpc_library")
#load("@com_github_grpc_grpc//bazel:grpc_build_system.bzl", "grpc_proto_library")

load("@rules_proto_grpc_python//:defs.bzl", "python_grpc_library")


package(default_visibility = ["//visibility:public"])

proto_library(
    name = "helloworld_proto",
    srcs = ["helloworld.proto"],
)

python_grpc_library(
    name = "helloworld_py_pb2_grpc",
    protos = [":helloworld_proto"],
)
