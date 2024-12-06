def evaluate_expression(num1: float, num2: float, operator: str) -> float:
    def divide(x: float, y: float) -> float:
        if y == 0:
            raise ZeroDivisionError("Division by zero")
        return x / y
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: divide(x, y),
    }
    if operator not in ops:
        raise ValueError("Unsupported operator")
    return ops[operator](num1, num2)

operator_precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}
