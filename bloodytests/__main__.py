"""Allow execution of tests from commandline.

Expected input
python -m bloodytests
"""

import os
import sys
import unittest

from bloodytests.testresult import BloodyTestResult
from bloodytests.testrunner import BloodyTestRunner


def main():
    try:
        pattern = sys.argv[1] + '.py'
    except IndexError:
        pattern = 'test*.py'
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    executing_dir = os.path.abspath('')

    tests = loader.discover(start_dir=executing_dir, pattern=pattern)
    suite.addTests(tests)

    result = BloodyTestRunner().run(suite)

    if result.wasSuccessful():
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
