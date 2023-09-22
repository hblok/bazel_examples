# An image with Bazel installed on Ubuntu 22.04

FROM ubuntu:22.04


# Basic packages and JDK
RUN \
    apt-get update && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y software-properties-common curl git apt-transport-https gnupg sudo
RUN \
    apt-get install -y openjdk-11-jdk-headless

# Bazel
RUN \
    curl -fsSL https://bazel.build/bazel-release.pub.gpg | gpg --dearmor > bazel.gpg && \
    sudo mv bazel.gpg /etc/apt/trusted.gpg.d/ && \
    echo "deb [arch=amd64] https://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list && \
    apt-get update && \
    apt-get install -y bazel


# nodejs, mocha
RUN \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y mocha nodejs

# More
RUN \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get install -y python3-dev gcc-10

# Our environment
COPY bazel_examples_test.sh /build/bazel_examples_test.sh
