#include <iostream>
#include <string>

#include "protobuf/phonebook/person.pb.h"

using namespace std;

int main(int argc, char* argv[]) {
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  phonebook::Person person;

  person.set_firstname("John");
  person.set_lastname("Doe");

  cout << endl;
  cout << "First name: " << person.firstname() << endl;
  cout << "Last name : " << person.lastname() << endl;
  cout << endl;
}
