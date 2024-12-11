import pytest
import time
from calculator.expression_evaluator import calculate_expression

RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"
BOLD = "\033[1m"
RESET = "\033[0m"

class TestCounter:
    def __init__(self):
        self.total = 0
        self.passed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            self.total += 1
            if report.passed:
                self.passed += 1

def main():
    print(CYAN + "=====================================" + RESET)
    print(CYAN + BOLD + "          Gindi Calculator" + RESET)
    print(CYAN + "=====================================" + RESET)
    print("Type an expression and press Enter.")
    print("Commands: " + BOLD + CYAN + "test" + RESET + ", " + BOLD + CYAN + "quit" + RESET + ", " + BOLD + CYAN + "exit" + RESET)
    print()

    while True:
        try:
            user_input = input(CYAN + ">> " + RESET).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break
        elif not user_input:
            continue
        elif user_input.lower() == "test":
            counter = TestCounter()
            exit_code = pytest.main(["tests"], plugins=[counter])
            if counter.total > 0:
                color = GREEN if exit_code == 0 else RED
                print(color + f"Tests Passed: {counter.passed}/{counter.total}" + RESET)
            else:
                print(RED + "No tests found." + RESET)
            continue

        start_time = time.perf_counter()
        try:
            result = calculate_expression(user_input)
            elapsed_s = time.perf_counter() - start_time
            # One-liner, clean UI: Result and timing in one line, similar to how some CLI tools do it
            print(f"{GREEN}Result: {result}{RESET} ({elapsed_s:.3f}s)")
        except Exception as e:
            elapsed_s = time.perf_counter() - start_time
            print(RED + f"Error: {e}" + RESET + f" ({elapsed_s:.3f}s)")

if __name__ == "__main__":
    main()
