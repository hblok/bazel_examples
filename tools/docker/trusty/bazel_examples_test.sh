#!/bin/sh

cd `dirname $0`

git clone https://github.com/hblok/bazel_examples.git
cd bazel_examples

tools/docker/test_all.sh
