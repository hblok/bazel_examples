cc_library(
    name = "hello",
    srcs = ["hello.cpp"],
    hdrs = ["hello.h"],
)

cc_test(
    name= "hello_test",
    srcs = ["hello_test.cpp"],
    deps = [
        ":hello",
        "@googletest//:gtest_main",
    ],
    size = "small",
)
