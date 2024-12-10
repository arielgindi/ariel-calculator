from calculator.expression_evaluator import calculate_expression

RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"
RESET = "\033[0m"

def main():
    # A simple welcome banner
    print(CYAN + "=======================================" + RESET)
    print(CYAN + "Welcome to the Super Console Calculator" + RESET)
    print(CYAN + "=======================================" + RESET)
    print("Type an expression and press Enter to calculate.")
    print("Special commands: 'quit' or 'exit'")
    print("Use Up/Down arrow keys to navigate through command history.")
    print()

    while True:
        try:
            user_input = input(CYAN + "Enter expression: " + RESET).strip()
        except (EOFError, KeyboardInterrupt):
            # If user presses Ctrl+D or Ctrl+C, just exit gracefully
            print("\nGoodbye!")
            break

        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break
        elif not user_input:
            # Just skip empty input
            continue

        try:
            result = calculate_expression(user_input)
            print(GREEN + f"Result: {result}" + RESET)
        except Exception as e:
            print(RED + f"Error: {e}" + RESET)

main()
