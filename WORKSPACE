# Downloads the source and compiles.
new_http_archive(
    name = "gtest",
    url = "https://github.com/google/googletest/archive/release-1.8.0.zip",
    sha256 = "f3ed3b58511efd272eb074a3a6d6fb79d7c2e6a0e374323d1e6bcbcc1ef141bf",
    build_file = "build_file/gtest.BUILD",
    strip_prefix = "googletest-release-1.8.0",
)

# Uses a local installation, and statically linked .a library files.
new_local_repository(
    name = "usr_lib_gtest",
    path = "/usr/lib",
    build_file_content = """
cc_library(
    name = "gtest",
    srcs = ["libgtest.a", "libgtest_main.a"],
    linkopts=["-lpthread"],
    linkstatic = 1,
    visibility = ["//visibility:public"],
)""",

)