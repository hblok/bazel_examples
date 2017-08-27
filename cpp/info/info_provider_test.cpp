#include <string>

#include <gtest/gtest.h>

#include "info_provider.h"


TEST(InfoProvider, GetInfo) {
  InfoProvider info;
  
  std::list<std::string> envars = info.getInfo();
  EXPECT_TRUE(envars.size() > 0);	
}


int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
