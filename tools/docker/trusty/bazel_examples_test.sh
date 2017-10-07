#!/bin/sh

cd `dirname $0`

FOUND_MOCHA=$(dirname `find / -path "*/mocha/bin/mocha"`)
echo "Found Mocha at $FOUND_MOCHA"
export PATH=$FOUND_MOCHA:/usr/local/node_modules/mocha/bin:$PATH

git clone https://github.com/hblok/bazel_examples.git
cd bazel_examples

tools/docker/test_all.sh
