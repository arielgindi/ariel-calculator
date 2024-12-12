from calculator.tokens import Token
from calculator.operations import OPERATORS

def convert_to_postfix(tokens: list[Token]) -> list[Token]:
    if not tokens:
        raise ValueError("Cannot convert an empty token list to postfix.")

    output: list[Token] = []
    stack: list[Token] = []
    for t in tokens:
        if t.token_type == "NUMBER":
            output.append(t)
        elif t.token_type == "OPERATOR":
            if t.value not in OPERATORS:
                raise ValueError(f"Unknown operator '{t.value}'.")
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
                raise ValueError("Mismatched parentheses: Missing '('")
            stack.pop()

    while stack:
        top = stack.pop()
        if top.token_type in ("LPAREN", "RPAREN"):
            raise ValueError("Mismatched parentheses in expression.")
        output.append(top)

    if not output:
        raise ValueError("Conversion to postfix resulted in an empty output, invalid expression.")

    return output
