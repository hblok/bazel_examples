cc_binary(
    name = "hello",
    srcs = ["hello.c"]
)


# Preferred; for libraries which can be downloaded and compiled.
cc_test(
    name= "http_archive_test",
    srcs = ["multiply_test.cpp"],
    deps = [
        "@googletest//:gtest_main",
    ],
    size = "small",
)

# Local library option.
#cc_test(
#    name= "usr_lib_test",
#    srcs = ["multiply_test.cpp"],
#    deps = [
#        "@usr_lib_gtest//:gtest",
#    ],
#    size = "small",
#)

# Not preferred.
#
# Generally, you do not want to do this, since the gtest library is brought in
# through the linker option, and thus have to be installed on the system which
# builds and runs the test.
#
# See the other gtest examples above for better solutions.
#
#cc_test(
#    name = "external_linkopts_test",
#    srcs = ["multiply_test.cpp"],
#    # Do not do this -- see above.
#    linkopts=["-lpthread", "-lgtest_main", "-lgtest" ],
#    size = "small",
#)
