py_library(
    name = "info_provider",
    srcs = ["info_provider.py"],
    srcs_version = "PY2AND3",
)

py_binary(
    name = "show_info",
    srcs = ["show_info.py"],
    deps = [":info_provider"],
    srcs_version = "PY2AND3",
)

py_binary(
    name = "hello_world",
    srcs = ["hello_world.py"],
    srcs_version = "PY2AND3",
)

py_test(
    name = "info_provider_test",
    srcs = ["info_provider_test.py"],
    deps = [":info_provider"],
    srcs_version = "PY2AND3",
    size = "small",
)

py_test(
    name = "person_test",
    srcs = ["person_test.py"],
    deps = ["//protobuf/phonebook:person_py_proto"],
    size = "small",
)
