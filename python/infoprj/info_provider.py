""" Gets some info. """

import os

class InfoProvider(object):

  def getInfo(self):
    return ["%s=%s" % (k, v)
            for k, v in os.environ.iteritems()]
