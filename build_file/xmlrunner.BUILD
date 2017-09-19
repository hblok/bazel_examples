# This file demonstrates the following concepts:
# - multiple targets within a new_http_archive repository, but only one public
# - a genrule to modify the downloaded library
# - custom stripping of the package path
# - Python 2 and 3 compatibility
# - arrays, for more readable targets

# The problem with the xmlrunner library is that it has its own unittest.py
# module. When this file is within the xmlrunner package, it's fine, however,
# if we'd like to strip the package name, and let the new_http_archive provide
# it instead, there is a conflict between xmlrunner/unittest.py and the Python
# unittest module.
#
# One alternative would be to keep the package, however, then it ends up in a
# "dual" package path, so "from xmlrunner import xmlrunner" is needed whenever
# Bazel builds the project (but it will fail using the normal PYTHONPATH). To
# keep the code working in both cases, this fix is needed.


ORIGINAL_FILES = [
    "xmlrunner/__init__.py",
    "xmlrunner/__main__.py",
    "xmlrunner/builder.py",
    "xmlrunner/result.py",
    "xmlrunner/runner.py",
    "xmlrunner/unittest.py",
    "xmlrunner/version.py",
]

OUTPUT_FILES = [
    "__init__.py",
    "__main__.py",
    "builder.py",
    "result.py",
    "runner.py",
    "version.py",
    "xunittest.py",
]

py_library(
    name = "downloaded_xmlrunner",
    srcs = ORIGINAL_FILES,
)


# This rule takes the original files, using an intermediate library, as
# input. The *.py files are copied to the output directory of this target,
# using $(@D), and then the rename of local unittest.py is applied.
#
# Note that a genrule cannot have the same files as input and output; coping
# the files out of the xmlrunner package resolves this. (Otherwise, we could
# have stripped the xmlrunner package on the new_http_archive level).
#
# Also, the intermediate :downloaded_xmlrunner target proves handy to specify
# the file locations of the *py files. Hard-coding the directory paths should
# be avoided.
#
genrule(
    name = "rename_unittest",
    srcs = [":downloaded_xmlrunner"],
    outs = OUTPUT_FILES,
    cmd = "cp $(locations :downloaded_xmlrunner) $(@D); \
           sed -i 's/\.unittest/xunittest/g' $(@D)/*py; \
           mv $(@D)/unittest.py $(@D)/xunittest.py"
)


# This target exposes the output of the genrule as a public (outside of
# this new_http_archive repository) py_library target. It has the same name
# as the repository, so that the short-hand dependency form can be used,
# i.e. "@xmlrunner". Finally, it marks the files compatible with both Python
# 2 and 3 code.
#
py_library(
    name = "xmlrunner",
    srcs = [":rename_unittest"],
    srcs_version = "PY2AND3",
    visibility = ["//visibility:public"],
)
