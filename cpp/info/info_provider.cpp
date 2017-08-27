#include <list>
#include <string>
#include <unistd.h>

#include "info_provider.h"


InfoProvider::InfoProvider() {
  extern char **environ;

  int i = 0;
  while(environ[i] != NULL) {
    info.push_front(environ[i]);
    i++;
  }
}

std::list<std::string> InfoProvider::getInfo() {
  return info;
}
