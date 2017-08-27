""" Shows some info. """

from python.infoprj import info_provider


class ShowInfo(object):

  def show(self):
    env = info_provider.InfoProvider().getInfo()
    for e in sorted(env):
      print e


def main():
  ShowInfo().show()


if __name__ == "__main__":
  main()
