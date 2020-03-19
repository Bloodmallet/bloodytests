import django

from bloodytests.testresult import BloodyTestResult
from bloodytests.testrunner import BloodyTestRunner


class BloodyDiscoverRunner(django.test.runner.DiscoverRunner):
    """Extension of djangos DiscoverRunner to use BloodyTestRunner and
    BloodyTestResult.
    """
    test_runner = BloodyTestRunner

    def get_resultclass(self):
        return BloodyTestResult
