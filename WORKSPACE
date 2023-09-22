load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

skylib_version = "1.4.2"

# Bazel Skylib: Common useful functions and rules for Bazel
skylib_version = "1.0.2"
http_archive(
    name = "bazel_skylib",
    sha256 = "97e70364e9249702246c0e9444bccdc4b847bed1eb03c5a3ece4f83dfe6abc44",
    urls = [
        "https://github.com/bazelbuild/bazel-skylib/releases/download/{}/bazel-skylib-{}.tar.gz"
            .format(skylib_version, skylib_version),
    ],
)

#load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")
#bazel_skylib_workspace()


# Google Test - Unit test framework for C++

gtest_version = "1.14.0"

http_archive(
    name = "gtest",
    url = "https://github.com/google/googletest/archive/refs/tags/v%s.zip" % gtest_version,
    sha256 = "1f357c27ca988c3f7c6b4bf68a9395005ac6761f034046e9dde0896e3aba00e4",
    build_file = "@//build_file:gtest.BUILD",
    strip_prefix = "googletest-%s" % gtest_version,
)


# Python unittest XML xUnit test result output format
# See the xmlrunner.BUILD file for details on the transformation of this target.
xmlrunner_version = "3.0.2"
http_archive(
    name = "github_xmlrunner",
    url = "https://github.com/xmlrunner/unittest-xml-reporting/archive/refs/tags/%s.tar.gz" % xmlrunner_version,
    sha256 = "dbe165386952ec5373d4db5b4ac0644b60b734f4b02b9e575b1d0dc873616ba4",
    build_file = "@//build_file:xmlrunner.BUILD",
    strip_prefix = "unittest-xml-reporting-%s" % xmlrunner_version,
)


# Disabled, since it would break the build if this is not already installed.

# Uses a local installation, and statically linked .a library files.
#new_local_repository(
#    name = "usr_lib_gtest",
#    path = "/usr/lib",
#    build_file_content = """
#cc_library(
#    name = "gtest",
#    srcs = ["libgtest.a", "libgtest_main.a"],
#    linkopts=["-lpthread"],
#    linkstatic = 1,
#    visibility = ["//visibility:public"],
#)""",
#
#)


# ZLIB
http_archive(
    name = "zlib",
    build_file = "@com_google_protobuf//:third_party/zlib.BUILD",
    sha256 = "c3e5e9fdd5004dcb542feda5ee4f0ff0744628baf8ed2dd5d66f8ca1197cb1a1",
    strip_prefix = "zlib-1.2.11",
    urls = [
        "https://mirror.bazel.build/zlib.net/zlib-1.2.11.tar.gz",
        "https://zlib.net/zlib-1.2.11.tar.gz",
    ],
)


# rules_jvm_external - Transitive Maven artifact resolution and publishing rules for Bazel.
rules_jvm_external_version = "4.2"
http_archive(
    name = "rules_jvm_external",
    strip_prefix = "rules_jvm_external-%s" % rules_jvm_external_version,
    sha256 = "cd1a77b7b02e8e008439ca76fd34f5b07aecb8c752961f9640dea15e9e5ba1ca",
    url = "https://github.com/bazelbuild/rules_jvm_external/archive/%s.zip" % rules_jvm_external_version,
)
load("@rules_jvm_external//:repositories.bzl", "rules_jvm_external_deps")
rules_jvm_external_deps()



# Google Protobuf language libraries
#
# From https://github.com/cgrushko/proto_library/blob/master/WORKSPACE
#

# proto_library rules implicitly depend on @com_google_protobuf//:protoc,
# which is the proto-compiler.
# This statement defines the @com_google_protobuf repo.

protobuf_version = "24.3"
protobuf_url = "https://github.com/protocolbuffers/protobuf/releases/download/v%s/protobuf-%s.zip" % (protobuf_version, protobuf_version)
protobuf_sha256_sum = "d6aac727167e7a91e407d482ab541c124cc7e101914ae37754b15b0e6d8d8546"

http_archive(
    name = "com_google_protobuf",
    url = protobuf_url,
    strip_prefix = "protobuf-%s" % protobuf_version,
    sha256 = protobuf_sha256_sum
)

#load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")
#protobuf_deps()

# cc_proto_library rules implicitly depend on @com_google_protobuf_cc//:cc_toolchain,
# which is the C++ proto runtime (base classes and common utilities).
http_archive(
    name = "com_google_protobuf_cc",
    url = protobuf_url,
    strip_prefix = "protobuf-%s" % protobuf_version,
    sha256 = protobuf_sha256_sum
)

# java_proto_library rules implicitly depend on @com_google_protobuf_java//:java_toolchain,
# which is the Java proto runtime (base classes and common utilities).
http_archive(
    name = "com_google_protobuf_java",
    url = protobuf_url,
    strip_prefix = "protobuf-%s" % protobuf_version,
    sha256 = protobuf_sha256_sum
)

# java_lite_proto_library rules implicitly depend on @com_google_protobuf_javalite//:javalite_toolchain,
# which is the JavaLite proto runtime (base classes and common utilities).
http_archive(
    name = "com_google_protobuf_javalite",
    url = protobuf_url,
    strip_prefix = "protobuf-%s" % protobuf_version,
    sha256 = protobuf_sha256_sum
)


# Google GRPC

grpc_version = "1.58.1"

http_archive(
    name = "com_github_grpc_grpc",
    url = "https://github.com/grpc/grpc/archive/refs/tags/v%s.zip" % grpc_version,
    strip_prefix = "grpc-%s" % grpc_version,
    sha256 = "7fa38089fd87e83ed17287276b0f0fda49099a8907df2131b89999ad774bfe33",
)

load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")
grpc_deps()
load("@com_github_grpc_grpc//bazel:grpc_extra_deps.bzl", "grpc_extra_deps")
grpc_extra_deps()


# rules_python

rules_python_version = "0.25.0"

http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/archive/refs/tags/{}.zip".format(rules_python_version),    
    strip_prefix = "rules_python-{}".format(rules_python_version),
    sha256 = "9ffcbf19b197153d7ceafb126eb05b7b5ce847aa4e1745f03feed298b4940e2c",
)
