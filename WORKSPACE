# Downloads the source and compiles.
new_http_archive(
    name = "gtest",
    url = "https://github.com/google/googletest/archive/release-1.8.0.zip",
    sha256 = "f3ed3b58511efd272eb074a3a6d6fb79d7c2e6a0e374323d1e6bcbcc1ef141bf",
    build_file = "build_file/gtest.BUILD",
    strip_prefix = "googletest-release-1.8.0",
)


#
# See the xmlrunner.BUILD file for details on the transformation of this target.
#
new_http_archive(
    name = "github_xmlrunner",
    url = "https://github.com/xmlrunner/unittest-xml-reporting/archive/2.1.0.tar.gz",
    sha256 = "d3cd068e081c1b60e7e9ab9ef10358d1268b481285aa3471a0f16a33ad9c8966",
    build_file = "build_file/xmlrunner.BUILD",
    strip_prefix = "unittest-xml-reporting-2.1.0",
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


# Google Protobuf language libraries
#
# From https://github.com/cgrushko/proto_library/blob/master/WORKSPACE
#

# proto_library rules implicitly depend on @com_google_protobuf//:protoc,
# which is the proto-compiler.
# This statement defines the @com_google_protobuf repo.
http_archive(
    name = "com_google_protobuf",
    urls = ["https://github.com/google/protobuf/archive/b4b0e304be5a68de3d0ee1af9b286f958750f5e4.zip"],
    strip_prefix = "protobuf-b4b0e304be5a68de3d0ee1af9b286f958750f5e4",
    sha256 = "ff771a662fb6bd4d3cc209bcccedef3e93980a49f71df1e987f6afa3bcdcba3a",
)

# cc_proto_library rules implicitly depend on @com_google_protobuf_cc//:cc_toolchain,
# which is the C++ proto runtime (base classes and common utilities).
http_archive(
    name = "com_google_protobuf_cc",
    urls = ["https://github.com/google/protobuf/archive/b4b0e304be5a68de3d0ee1af9b286f958750f5e4.zip"],
    strip_prefix = "protobuf-b4b0e304be5a68de3d0ee1af9b286f958750f5e4",
    sha256 = "ff771a662fb6bd4d3cc209bcccedef3e93980a49f71df1e987f6afa3bcdcba3a",
)

# java_proto_library rules implicitly depend on @com_google_protobuf_java//:java_toolchain,
# which is the Java proto runtime (base classes and common utilities).
http_archive(
    name = "com_google_protobuf_java",
    urls = ["https://github.com/google/protobuf/archive/b4b0e304be5a68de3d0ee1af9b286f958750f5e4.zip"],
    strip_prefix = "protobuf-b4b0e304be5a68de3d0ee1af9b286f958750f5e4",
    sha256 = "ff771a662fb6bd4d3cc209bcccedef3e93980a49f71df1e987f6afa3bcdcba3a",
)

# java_lite_proto_library rules implicitly depend on @com_google_protobuf_javalite//:javalite_toolchain,
# which is the JavaLite proto runtime (base classes and common utilities).
http_archive(
    name = "com_google_protobuf_javalite",
    urls = ["https://github.com/google/protobuf/archive/45ff30697af6590a927c73584351f2670768f719.zip"],
    strip_prefix = "protobuf-45ff30697af6590a927c73584351f2670768f719",
    sha256 = "2244bc5077087be2e5ca8fab9cb4b614443b572cedd83a01d773d3c6c971635c",
)
