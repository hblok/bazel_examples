#!/bin/bash
#
# This script can be executed manually stand-alone.

THIS_DIR="$(dirname $0)"
cd $THIS_DIR

bazel run server &
SERVER_PID=$!

sleep 1
bazel run client

kill $SERVER_PID

echo -e "\n\n"
