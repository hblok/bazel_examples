cmake_minimum_required(VERSION 3.0)

add_library(Hello OBJECT
  hello.h
  hello.cpp)


enable_testing()
if (NOT GTEST_ADD)
  message(">> In Hello")
  add_subdirectory(/usr/src/gtest ${CMAKE_CURRENT_BINARY_DIR}/gtest)
  set(GTEST_ADD 1 PARENT_SCOPE)
endif()

add_executable(hello_test.bin
  hello_test.cpp
  $<TARGET_OBJECTS:Hello>)
target_link_libraries(hello_test.bin gtest)

add_test(hello_test
  hello_test.bin
  $<TARGET_OBJECTS:Hello>)
