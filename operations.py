def safe_divide(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Division by zero")
    return x / y

def safe_modulo(x: float, y: float) -> float:
    if y == 0:
        raise ZeroDivisionError("Modulo by zero")
    return x % y

def factorial(n: float) -> float:
    # Factorial requires non-negative integers.
    if n < 0 or n != int(n):
        raise ValueError("Factorial is not defined for negative or non-integer values")
    n_int: int = int(n)
    res: int = 1
    for i in range(1, n_int + 1):
        res *= i
    return float(res)

OPERATORS: dict[str, dict[str, object]] = {
    '+': {'precedence': 1, 'function': lambda x, y: x + y, 'unary': False},
    '-': {'precedence': 1, 'function': lambda x, y: x - y, 'unary': False},
    '*': {'precedence': 2, 'function': lambda x, y: x * y, 'unary': False},
    '/': {'precedence': 2, 'function': safe_divide, 'unary': False},
    '^': {'precedence': 3, 'function': lambda x, y: pow(x, y), 'unary': False},
    '%': {'precedence': 4, 'function': safe_modulo, 'unary': False},
    '$': {'precedence': 5, 'function': lambda x, y: max(x, y), 'unary': False},
    '&': {'precedence': 5, 'function': lambda x, y: min(x, y), 'unary': False},
    '@': {'precedence': 5, 'function': lambda x, y: (x + y) / 2, 'unary': False},
    '!': {'precedence': 6, 'function': lambda x: factorial(x), 'unary': True},
    '~': {'precedence': 6, 'function': lambda x: -x, 'unary': True}
}

ALL_OPERATORS: str = ''.join(OPERATORS.keys())
FILTERED_OPERATORS: str = ''.join(o for o in ALL_OPERATORS if o not in '+-')
