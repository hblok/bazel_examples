# bazel_examples
Example Bazel use cases and BUILD files in different languages.

Currently includes examples for
  - [C++](cpp)
  - [Java](java)
  - [Maven dependencies for Java](com/example/apache_collections)
  - [Python](python)
  - [Protocol Buffers (aka protobuf)](protobuf/phonebook)
  - [Python with Protobuf + GRPC](python/helloworld_grpc)
  - [JavaScript Mocha tests](js/mocha)
  
  - [mocha_test - a custom target macro](js/mocha/mocha_test.bzl)

  - [GitHub Actions Workflow](.github/workflows/main.yml)
  - [Ubuntu 20.04 based Docker image with bazel installation and test run](tools/docker/ubuntu_20.04)
  - [Travis CI test run example](.travis.yml) (Deprecated)

  - Tests result: ![test result](https://github.com/hblok/bazel_examples/actions/workflows/main.yml/badge.svg)


Contributions welcome!


## Installation

Follow Bazel installation instructions here:  
https://docs.bazel.build/versions/master/install.html

Then:  

    git clone https://github.com/hblok/bazel_examples.git
    cd bazel_examples


## Some basic commands

    bazel query ...

    bazel test ...

    bazel run //cpp/info:show_info
    
    bazel run //java/com/example/info:HelloWorld
    
    bazel run //python/infoprj:info_provider

(Only one of the bazel commands above is sufficent -- each command is self-contained).


## Comparative studies

For some parts, other build systems structures are also included, to study the difference between Bazel. Currently, this includes:

  - [CMake / CTest](https://github.com/hblok/bazel_examples/search?q=ctest)

