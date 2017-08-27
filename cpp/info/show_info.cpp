#include <iostream>
#include <list>
#include <string>

#include "info_provider.h"


int main( int argc, char **argv ) {
  InfoProvider info;
  std::list<std::string> info_list = info.getInfo();

  for(std::list<std::string>::const_iterator i = info_list.begin();
      i != info_list.end(); ++i) {
    std::cout << i->c_str() << std::endl;
  }
}
