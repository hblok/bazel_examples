#!/bin/sh

sudo docker build -t bazel_examples .
sudo docker run -it bazel_examples /build/bazel_examples_test.sh

