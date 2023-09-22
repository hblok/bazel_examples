#!/bin/sh

docker build -t bazel_examples .
docker run -it bazel_examples /build/bazel_examples_test.sh

