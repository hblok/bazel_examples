#!/bin/bash
# 
# This script is to be executed from within bazel.
#
# Usage:
#   bazel test --test_output all test

env
BASE_DIR=$RUNFILES_DIR/$TEST_WORKSPACE/python/helloworld_grpc
ls -l $BASE_DIR

$BASE_DIR/server &
SERVER_PID=$!

sleep 1
$BASE_DIR/client

kill $SERVER_PID

echo -e "\n\n"
