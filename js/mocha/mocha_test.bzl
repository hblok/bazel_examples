# Runs all the srcs files as Mocha tests. By default, the tdd (Test Driven
# Development) user interface is used. It can be changed with the ui option.
#
# In this example, it is assumed that mocha (and nodejs) is already installed
# on the system, and on the PATH. The test will fail otherwise. (See the
# mocha.sh script).

def mocha_test(name, srcs, deps=[], ui="tdd"):

  native.sh_test(
    name = name,
    srcs = ["mocha.sh"],
    data = srcs,
    args = ["-u", ui] + ["$(location %s)" % s for s in srcs],
    deps = deps,
  )
