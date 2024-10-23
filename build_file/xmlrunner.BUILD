package(default_visibility = ["//visibility:public"])

# The path in the glob has to include the module directory, and recursively
# include all .py files. This retains the package directory as a top
# level Python package name, and makes the new_http_archive name (in the
# WORKSPACE file) as well as the py_library name here irrelevant in the Python
# import. Furthermore, when both the new_http_archive and py_library names
# are the same, the library dependency can be referenced by the short-form
# @github_xmlrunner in other BUILD files.
#
# (A previous version of this file misleadingly transformed the project
# directory, but that resulted in problems with conflicting module names at
# the top level).
#
py_library(
    name = "github_xmlrunner",
    srcs = glob(["xmlrunner/**/*.py"]),
)
