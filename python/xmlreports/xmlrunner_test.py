""" Demonstrates use of the xmlrunner library.

It should be noted, that this is somewhat redundant, since bazel already
produces XML result output on the same xUnit format under
  bazel-testlogs/python/xmlreports/xmlrunner_test/test.xml
(Where the path after bazel-testlogs mirrors the path of this test).
"""

import os
import unittest

# TODO: Avoid the dual package here. However, the problem seems to be the
# internal unittest.py module of the xmlrunner project. It gets mixed up with
# the offical python unittest package. Otherwise, we could have stripped the
# xmlrunner path in the new_http_archive.
from xmlrunner_github import xmlrunner


class TestXmlRunner(unittest.TestCase):

  def test_hello(self):
    print "Hello"
    self.assertTrue(True)


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='/tmp/test-reports'),
        failfast=False, buffer=True, catchbreak=False)
