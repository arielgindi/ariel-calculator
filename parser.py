from tokens import Token
from operations import OPERATORS

def convert_to_postfix(tokens: list[Token]) -> list[Token]:
    output: list[Token] = []
    stack: list[Token] = []
    for t in tokens:
        if t.token_type == "NUMBER":
            output.append(t)
        elif t.token_type == "OPERATOR":
            while stack and stack[-1].token_type == "OPERATOR":
                if (stack[-1].operator_precedence is not None and
                    t.operator_precedence is not None and
                    stack[-1].operator_precedence >= t.operator_precedence):
                    output.append(stack.pop())
                else:
                    break
            stack.append(t)
        elif t.token_type == "LPAREN":
            stack.append(t)
        elif t.token_type == "RPAREN":
            while stack and stack[-1].token_type != "LPAREN":
                output.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses")
            stack.pop()

    while stack:
        top = stack.pop()
        if top.token_type in ("LPAREN", "RPAREN"):
            raise ValueError("Mismatched parentheses")
        output.append(top)

    return output

def postfix_calculator(tokens: list[Token]) -> float:
    stack: list[float] = []
    for t in tokens:
        if t.token_type == "NUMBER":
            stack.append(t.value)  # value is float in this case
        elif t.token_type == "OPERATOR":
            op_info = OPERATORS[t.value]
            if op_info['unary']:
                # Unary operator needs one operand.
                if len(stack) < 1:
                    raise ValueError("Not enough values for unary operator")
                a = stack.pop()
                res = op_info['function'](a)
                stack.append(res)
            else:
                # Binary operator needs two operands.
                if len(stack) < 2:
                    raise ValueError("Not enough values for binary operator")
                b = stack.pop()
                a = stack.pop()
                res = op_info['function'](a, b)
                stack.append(res)

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    return stack[0]
