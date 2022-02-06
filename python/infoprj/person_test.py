""" Unit tests for person_py_proto """

import inspect
import unittest

from google.protobuf import json_format
from protobuf.phonebook import person_pb2


class TestPerson(unittest.TestCase):

  def testConsturctor(self):
    person = person_pb2.Person()
    print(dir(person))

  def testFields(self):
    person = person_pb2.Person()
    person.firstname = "John"
    person.lastname = "Doe"
    person.id = 123
    person.email = "john.doe@example.com"

    address = person.address
    address.city = "London"

    print("> Person:\n", person)

    print("> JSON: \n", json_format.MessageToJson(person))


if __name__ == "__main__":
  unittest.main()
