cc_library(
    name = "info_provider",
    srcs = ["info_provider.cpp"],
    hdrs = ["info_provider.h"],
    copts = ["-std=c++17"],
)

cc_binary(
    name = "show_info",
    srcs = ["show_info.cpp"],
    deps = [":info_provider"],
)

cc_test(
    name= "info_provider_test",
    srcs = ["info_provider_test.cpp"],
    deps = [
        ":info_provider",
        "@gtest//:gtest_main",
    ],
    size = "small",
)
