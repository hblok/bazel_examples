#ifndef INFO_PROVIDER_H
#define INFO_PROVIDER_H

#include <list>
#include <string>

class InfoProvider {

 public:
  InfoProvider();

  std::list<std::string> getInfo();

 private:
  std::list<std::string> info;
};

#endif // INFO_PROVIDER_H
