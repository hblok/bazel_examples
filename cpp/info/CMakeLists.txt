cmake_minimum_required(VERSION 3.0)

add_library(Info OBJECT
  info_provider.h
  info_provider.cpp)

add_executable(info_provider.bin
  show_info.cpp
  $<TARGET_OBJECTS:Info>)


enable_testing()
add_subdirectory(/usr/src/gtest ${CMAKE_CURRENT_BINARY_DIR}/gtest)

add_executable(info_provider_test.bin
  info_provider_test.cpp
  $<TARGET_OBJECTS:Info>)
target_link_libraries(info_provider_test.bin gtest)

add_test(info_provider_test
  info_provider_test.bin
  $<TARGET_OBJECTS:Info>)

