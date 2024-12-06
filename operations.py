def safe_divide(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Division by zero")
    return x / y

# Define operator precedence
OPERATOR_PRECEDENCE = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

# Define operator functions
OPERATOR_FUNCTIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': safe_divide
}

def evaluate_expression(num1: float, num2: float, operator: str) -> float:
    if operator not in OPERATOR_FUNCTIONS:
        raise ValueError("Unsupported operator")
    return OPERATOR_FUNCTIONS[operator](num1, num2)
