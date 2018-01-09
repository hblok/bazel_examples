""" Reads a file from included data dependencies. """

import os
import unittest


class TestReadFile(unittest.TestCase):

  def setUp(self):
    self.workdir = os.path.join(
        os.environ["TEST_SRCDIR"], os.environ["TEST_WORKSPACE"])
    self.file_name = os.path.join(self.workdir, "data/words")

  def test_print_env(self):
    for e in os.environ.items():
      print("=".join(e))
    
    for root, dirs, files in os.walk(self.workdir):
      print(root)
      for f in files:
        print("  ", f)
    
  def test_file_exists(self):
    self.assertTrue(os.path.isfile(self.file_name))

  def test_read_file(self):
    with open(self.file_name) as f:
      lines = f.readlines()

      self.assertEquals(100, len(lines))


if __name__ == "__main__":
  unittest.main()
