#
# Inspired by the "Protocol Buffers in Bazel" blog article example on the Bazel
# site, with the original at the Github link below.
#
# https://blog.bazel.build/2017/02/27/protocol-buffers.html
#
# https://github.com/cgrushko/proto_library/tree/master/src

package(default_visibility = ["//visibility:public"])

load("@com_google_protobuf//:protobuf.bzl", "py_proto_library")

# Convention:
# A java_proto_library that wraps a proto_library named foo_proto
# should be called foo_java_proto.
#
# Note that you only need a java_proto_library for the protos
# you directly use in your code - a java_proto_library converts
# an entire proto graph.
java_proto_library(
    name = "person_java_proto",
    deps = [":person_proto"],
)

# Convention:
# A java_lite_proto_library that wraps a proto_library named foo_proto
# should be called foo_java_proto_lite.
java_lite_proto_library(
    name = "person_java_proto_lite",
    deps = [":person_proto"],
)

# Convention:
# A cc_proto_library that wraps a proto_library named foo_proto
# should be called foo_cc_proto.
cc_proto_library(
    name = "person_cc_proto",
    deps = [":person_proto"],
)

# A py_proto_library, from "@com_google_protobuf//:protobuf.bzl" (see above),
# that compiles the specified .proto files and exports a library which can be
# used by other py targets.
# Note that, this library will work with Protobuf Well Known Types, or GRPC.
# For examples of those, see the directory "grpc" in this repo instead.
py_proto_library(
    name = "person_py_proto",
    srcs = [
    	 "person.proto",
	 "address.proto",
	 "zip_code.proto"
    ]
)

# Conventions:
# 1. One proto_library rule per .proto file.
# 2. A file named foo.proto will be in a rule named foo_proto.
proto_library(
    name = "person_proto",
    srcs = ["person.proto"],
    deps = [":address_proto"],
)

proto_library(
    name = "address_proto",
    srcs = ["address.proto"],
    deps = [":zip_code_proto"],
)

proto_library(
    name = "zip_code_proto",
    srcs = ["zip_code.proto"],
)
