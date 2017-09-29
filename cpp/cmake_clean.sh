#!/bin/bash

function remove_cmake {
  rm -rf Makefile CMakeFiles CTestTestfile.cmake cmake_install.cmake libInfo.a CMakeCache.txt info_provider*.bin Testing gtest
}

remove_cmake
cd info; remove_cmake
