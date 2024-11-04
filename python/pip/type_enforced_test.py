""" API test for type_enforced. """

import unittest

import type_enforced


class TypeEnforcedTest(unittest.TestCase):

    def test_ok(self):
        self.person("bob", 123)

    def test_invalid(self):
        self.assertRaises(TypeError, self.person, ("ann", "111"))

    @type_enforced.Enforcer
    def person(self, name:str, age:int):
        print(name, age)


if __name__ == "__main__":
    unittest.main()
