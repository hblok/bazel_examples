java_library(
    name = "info",
    srcs = ["InfoProvider.java"],
    visibility = ["//javatest/com/example/info:__pkg__"]
)

java_binary(
    name = "ShowInfo",
    srcs = ["ShowInfo.java"],
    deps = [":info"]
)

java_binary(
    name = "HelloWorld",
    srcs = ["HelloWorld.java"]
)


