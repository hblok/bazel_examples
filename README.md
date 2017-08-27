# bazel_examples
Example Bazel BUILD files and code structures

Contributions welcome!

## Installation
Follow Bazel installation instructions here:  
https://docs.bazel.build/versions/master/install.html

## Some basic commands
    git clone https://github.com/hblok/bazel_examples.git
    cd bazel_examples

    bazel query ...

    bazel test ...

    bazel run //cpp/info:show_info
    
    bazel run //java/com/example/info:HelloWorld
    
    bazel run //python/infoprj:info_provider

(Only one of the bazel commands above is sufficent -- each command is self-contained).
