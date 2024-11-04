# DEPRECATED:
# Note, although this is still a valid example of a custom test target around a
# Bash script, it is no longer a good way to run Mocha tests. Since this was
# initially written, the Aspect rules, delivered through NPM, has a better implementation.
#
# For a real-life example of that, see our other repository here:
# https://github.com/hblok/cloud_tycoon/blob/main/web/ui/BUILD


# Include this line in other BUILD files which uses the
# mocha_test target.
load("//js/mocha:mocha_test.bzl", "mocha_test")

package(default_visibility = ["//visibility:private"])


mocha_test(
  name = "tautology_test",
  srcs = ["example_test.js"],
)

sh_binary(
  name = "mocha",
  srcs = ["mocha.sh"],
)
