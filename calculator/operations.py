def safe_divide(x: float | int, y: float | int) -> float | int:
    if y == 0:
        raise ZeroDivisionError("Division by zero")
    return x / y

def safe_modulo(x: float | int, y: float | int) -> float | int:
    if y == 0:
        raise ZeroDivisionError("Modulo by zero")
    return x % y

def factorial(n: float | int) -> float | int:
    # Factorial requires non-negative integers.
    if n < 0 or n != int(n):
        raise ValueError("Factorial is not defined for negative or non-integer values")
    n_int: int = int(n)
    res: int = 1
    for i in range(1, n_int + 1):
        res *= i
    return res

def sum_digits(n: float | int) -> float | int:
    # Convert the number to string, handle sign and decimal point
    negative = (n < 0)
    s = str(abs(n))
    s = s.replace('.', '')
    digit_sum = sum(int(d) for d in s if d.isdigit())
    return -digit_sum if negative else digit_sum

OPERATORS: dict[str, dict[str, object]] = {
    '+': {'precedence': 1, 'associativity': 'left',  'unary': False, 'function': lambda x, y: x + y},
    '-': {'precedence': 1, 'associativity': 'left',  'unary': False, 'function': lambda x, y: x - y},
    '*': {'precedence': 2, 'associativity': 'left',  'unary': False, 'function': lambda x, y: x * y},
    '/': {'precedence': 2, 'associativity': 'left',  'unary': False, 'function': safe_divide},
    '^': {'precedence': 3, 'associativity': 'right', 'unary': False, 'function': lambda x, y: pow(x, y)},
    '%': {'precedence': 4, 'associativity': 'left',  'unary': False, 'function': safe_modulo},
    '$': {'precedence': 5, 'associativity': 'left',  'unary': False, 'function': lambda x, y: max(x, y)},
    '&': {'precedence': 5, 'associativity': 'left',  'unary': False, 'function': lambda x, y: min(x, y)},
    '@': {'precedence': 5, 'associativity': 'left',  'unary': False, 'function': lambda x, y: (x + y) / 2},
    '!': {'precedence': 6, 'associativity': 'right', 'unary': True,  'function': lambda x: factorial(x)},
    '~': {'precedence': 6, 'associativity': 'right', 'unary': True,  'function': lambda x: -x},
    '#': {'precedence': 6, 'associativity': 'right', 'unary': True,  'function': lambda x: sum_digits(x)}
}

ALL_OPERATORS: str = ''.join(OPERATORS.keys())
FILTERED_OPERATORS: str = ''.join(o for o in ALL_OPERATORS if o not in '+-')
