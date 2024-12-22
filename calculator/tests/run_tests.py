import pytest

RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"
BOLD = "\033[1m"
RESET = "\033[0m"


class TestCounter:
    """Custom pytest plugin to count total/passed tests."""
    __test__ = False

    def __init__(self):
        self.total = 0
        self.passed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            self.total += 1
            if report.passed:
                self.passed += 1


def run_tests():
    """Run the test suite using pytest and display the result."""
    counter = TestCounter()
    exit_code = pytest.main(["calculator/tests"], plugins=[counter])
    if counter.total == 0:
        print(f"{RED}No tests found.{RESET}")
        return

    color = GREEN if exit_code == 0 else RED
    print(f"{color}Tests Passed: {counter.passed}/{counter.total}{RESET}")
