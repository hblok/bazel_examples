#!/bin/bash

function remove_cmake {
  cd $1

  rm -rf Makefile CMakeFiles CTestTestfile.cmake cmake_install.cmake libInfo.a CMakeCache.txt info_provider*.bin hello*.bin Testing gtest

  cd -
}

remove_cmake .
remove_cmake hello
remove_cmake info
