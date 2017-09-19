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
    name = "xmlrunner",
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
