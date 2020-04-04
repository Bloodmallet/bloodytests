from django.test.runner import DiscoverRunner

from bloodytests.testresult import BloodyTestResult
from bloodytests.testrunner import BloodyTestRunner


class BloodyDiscoverRunner(DiscoverRunner):
    """Extension of djangos DiscoverRunner to use BloodyTestRunner and
    BloodyTestResult.
    """
    test_runner = BloodyTestRunner

    def get_resultclass(self):
        return BloodyTestResult
