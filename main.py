import time
from calculator.core.expression_calculator import calculate_expression
from calculator.tests.run_tests import run_tests

RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"
BOLD = "\033[1m"
RESET = "\033[0m"


def print_welcome():
    """Print the welcome banner and usage instructions."""
    print(f"{CYAN}====================================={RESET}")
    print(f"{CYAN}{BOLD}          Gindi Calculator{RESET}")
    print(f"{CYAN}====================================={RESET}")
    print("Type an expression and press Enter.")
    print(f"Commands: {BOLD}{CYAN}test{RESET}, {BOLD}{CYAN}exit{RESET}")
    print()


def main():
    print_welcome()

    while True:
        try:
            user_input = input(f"{CYAN}>> {RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        user_input_lower = user_input.lower()

        if user_input_lower in {"quit", "exit"}:
            print("Goodbye!")
            break

        if user_input_lower == "test":
            run_tests()
            continue

        start_time = time.perf_counter()
        try:
            result = calculate_expression(user_input)
            elapsed_s = time.perf_counter() - start_time
            print(f"{GREEN}Result: {result}{RESET} ({elapsed_s:.3f}s)")
        except Exception as e:
            elapsed_s = time.perf_counter() - start_time
            print(f"{RED}Error: {e}{RESET} ({elapsed_s:.3f}s)")


if __name__ == "__main__":
    main()
