#!/usr/bin/env python
#
# LSST Data Management System
# Copyright 2008, 2009, 2010 LSST Corporation.
#
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <http://www.lsstcorp.org/LegalNotices/>.
#

import unittest


class ThreadsTestCase(unittest.TestCase):

    def testApi(self):
        from lsst.base import haveThreads
        self.assertIsInstance(haveThreads(), bool)

        from lsst.base import setNumThreads  # noqa F401
# Raises lsst::base::NoThreadsException which is untranslated
# when threading library is missing, this needs fixing!
#        self.assertIs(setNumThreads(4), None)

        from lsst.base import getNumThreads
        self.assertIsInstance(getNumThreads(), int)

        from lsst.base import disableImplicitThreading
        self.assertIsInstance(disableImplicitThreading(), bool)


if __name__ == "__main__":
    unittest.main()
