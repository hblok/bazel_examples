# Include this line in other BUILD files which uses the
# mocha_test target.
#
load("//js/mocha:mocha_test.bzl", "mocha_test")

# Use the mocha_test target by loading the .bzl file as seen
# above. Do not depend on the internal targets below.
#
package(default_visibility = ["//visibility:private"])


mocha_test(
  name = "tautology_test",
  srcs = ["example_test.js"],
)

sh_binary(
  name = "mocha",
  srcs = ["mocha.sh"],
)
