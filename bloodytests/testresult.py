import time
import unittest


class BloodyTestResult(unittest.runner.TextTestResult):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_times = []

    def startTest(self, test):
        self._test_started_at = time.time()
        super().startTest(test)

    def addSuccess(self, test):
        elapsed = time.time() - self._test_started_at
        name = self.getDescription(test)
        self.test_times.append((name, elapsed))
        super().addSuccess(test)

    def getTestTimes(self):
        return self.test_times
