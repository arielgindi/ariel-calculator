from calculator.utils import simplify_signs
from calculator.tokens import tokenize, Token
from calculator.postfix_parser import convert_to_postfix, postfix_calculator

def calculate_expression(expression: str) -> float:
    expression = expression.replace(" ", "")
    if not expression:
        return False
    simplified_expr: str = simplify_signs(expression)
    tokens: list[Token] = tokenize(simplified_expr)
    postfix_tokens: list[Token] = convert_to_postfix(tokens)
    return postfix_calculator(postfix_tokens)
