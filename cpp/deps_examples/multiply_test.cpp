#include <gtest/gtest.h>

int multiply(int a, int b) {
  return a * b;
}

TEST(HelloTest, Multiply) {
  EXPECT_EQ(2, multiply(1, 2));	
}


int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
