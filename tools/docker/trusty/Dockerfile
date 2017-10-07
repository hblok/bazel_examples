# An image with Bazel installed on Ubuntu 14.04 (Trusty).
# This is do demonstrate testing on the Travis CI system.

FROM ubuntu:14.04


# Basic packages and Oracle JDK8
RUN \
    echo debconf shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections; \
    echo debconf shared/accepted-oracle-license-v1-1 seen true | /usr/bin/debconf-set-selections; \
    apt-get update && \
    apt-get install -y software-properties-common curl git && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y oracle-java8-installer


# Bazel
RUN \
    echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | tee /etc/apt/sources.list.d/bazel.list ; \
    curl https://bazel.build/bazel-release.pub.gpg | apt-key add - ; \
    apt-get update && \
    apt-get install -y bazel


# Our dependencies: nodejs, mocha
RUN \
    apt-get install -y npm python3-six && \
    curl -sL https://deb.nodesource.com/setup_7.x | bash - ; \
    apt-get install -y nodejs && \
    cd /usr/local; npm install mocha


# Our environment
COPY bazel_examples_test.sh /build/bazel_examples_test.sh
