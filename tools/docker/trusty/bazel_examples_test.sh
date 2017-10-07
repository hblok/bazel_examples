#!/bin/sh

cd `dirname $0`

export PATH=/usr/local/node_modules/mocha/bin:$PATH

git clone https://github.com/hblok/bazel_examples.git
cd bazel_examples

tools/docker/test_all.sh
