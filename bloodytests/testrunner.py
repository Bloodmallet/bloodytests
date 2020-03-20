import unittest
from bloodytests.testresult import BloodyTestResult


class BloodyTestRunner(unittest.TextTestRunner):

    def __init__(self, slow_test_threshold=0.3, resultclass=BloodyTestResult, *args, **kwargs):
        self.slow_test_threshold = slow_test_threshold
        super().__init__(resultclass=resultclass, *args, **kwargs)

    def run(self, test):
        result = super().run(test)

        times = sorted(result.getTestTimes(), key=lambda x: x[1])

        if not times:
            return result

        if times[0][1] >= self.slow_test_threshold:
            self.stream.writeln("\nSlow Tests (>{:.03f}s):".format(self.slow_test_threshold))

            for name, elapsed in times:
                if elapsed >= self.slow_test_threshold:
                    self.stream.writeln("  {:.03f}s {}".format(elapsed, name))

        return result
