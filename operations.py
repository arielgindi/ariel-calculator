def safe_divide(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Division by zero")
    return x / y

def safe_modulo(x: float, y: float) -> float:
    # similar check for modulo by zero
    if y == 0:
        raise ZeroDivisionError("Modulo by zero")
    return x % y

OPERATORS = {
    '+': {'precedence': 1, 'function': lambda x, y: x + y},
    '-': {'precedence': 1, 'function': lambda x, y: x - y},
    '*': {'precedence': 2, 'function': lambda x, y: x * y},
    '/': {'precedence': 2, 'function': safe_divide},
    '^': {'precedence': 3, 'function': lambda x, y: x ** y},
    '%': {'precedence': 4, 'function': safe_modulo},
    '$': {'precedence': 5, 'function': lambda x, y: max(x, y)},
    '&': {'precedence': 5, 'function': lambda x, y: min(x, y)},
    '@': {'precedence': 5, 'function': lambda x, y: (x + y) / 2}
}

ALL_OPERATORS = ''.join(OPERATORS.keys())
FILTERED_OPERATORS = ''.join(c for c in ALL_OPERATORS if c not in '+-')


def evaluate_expression(num1: float, num2: float, operator: str) -> float:
    if operator not in OPERATORS:
        raise ValueError("Unsupported operator")
    return OPERATORS[operator]['function'](num1, num2)