from calculator.operations import OPERATORS
from calculator.tokens import Token
from calculator.utils.parse_number import parse_number


def postfix_calculator(tokens: list[Token]) -> float | int:
    stack: list[float | int] = []
    for t in tokens:
        if t.token_type == "NUMBER":
            stack.append(t.value)
        elif t.token_type == "OPERATOR":
            op_info = OPERATORS[t.value]
            if op_info['unary']:
                if len(stack) < 1:
                    raise ValueError(f"Not enough operands for unary operator '{t.value}'.")
                a = stack.pop()
                try:
                    res = op_info['function'](a)
                except Exception as e:
                    raise ValueError(f"{e}, Error calculation unary operator '{t.value}' to {a}")
                stack.append(res)
            else:
                if len(stack) < 2:
                    raise ValueError(f"Operands are missing for '{t.value}'.")
                b = stack.pop()
                a = stack.pop()
                try:
                    res = op_info['function'](a, b)
                except Exception as e:
                    raise ValueError(f"{e}, Error calculation operator '{t.value}' to {a} and {b}")
                stack.append(res)

    if len(stack) != 1:
        raise ValueError("calculation didn't result in a single value. Expression may be invalid.")

    return parse_number(stack[0])