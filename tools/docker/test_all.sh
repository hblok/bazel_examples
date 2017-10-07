#!/bin/sh

export PATH=/usr/local/node_modules/mocha/bin:$PATH

TEST_OPTIONS="--force_python py3 --python_path /usr/bin/python3 --test_output=errors --verbose_failures --genrule_strategy=standalone --spawn_strategy=standalone"
bazel --batch test ${TEST_OPTIONS} ...
