py_library(
    name = "info_provider",
    srcs = ["info_provider.py"],
)

py_binary(
    name = "show_info",
    srcs = ["show_info.py"],
    deps = [":info_provider"]
)

py_binary(
    name = "hello_world",
    srcs = ["hello_world.py"],
)

py_test(
    name = "info_provider_test",
    srcs = ["info_provider_test.py"],
    deps = [":info_provider"],
    size = "small",
)
