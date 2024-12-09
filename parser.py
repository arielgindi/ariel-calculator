from tokens import Token
from operations import evaluate_expression

def convert_to_postfix(tokens: list[Token]) -> list[Token]:
    output = []
    stack = []
    for t in tokens:
        if t.token_type == "NUMBER":
            output.append(t)
        elif t.token_type == "OPERATOR":
            # Operator
            while stack and stack[-1].token_type == "OPERATOR" and stack[-1].operator_precedence >= t.operator_precedence:
                output.append(stack.pop())
            stack.append(t)
        elif t.token_type == "LPAREN":
            stack.append(t)
        elif t.token_type == "RPAREN":
            while stack and stack [-1].token_type != "LPAREN":
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
    stack = []
    for t in tokens:
        if t.token_type == "NUMBER":
            stack.append(t)
        else:
            if len(stack) < 2:
                raise ValueError("Not enough values")
            b = stack.pop().value
            a = stack.pop().value
            res = evaluate_expression(a, b, t.value)
            stack.append(Token("NUMBER", res))
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    return stack[0].value