""" Unit tests for info_provider.py. """

import unittest

from python.infoprj import info_provider


class TestInfoProvider(unittest.TestCase):

  def setUp(self):
    self.provider = info_provider.InfoProvider()

  def testGetInfo(self):
    self.assertTrue(len(self.provider.getInfo()) > 0)


if __name__ == "__main__":
  unittest.main()
