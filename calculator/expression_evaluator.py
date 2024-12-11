from calculator.tokens import tokenize, Token
from calculator.postfix_parser import convert_to_postfix, postfix_calculator
from calculator.utils.remove_spaces import remove_spaces
from calculator.utils.simplify_signs import simplify_signs


def calculate_expression(expression: str) -> float | int:
    if not expression:
        raise ValueError("Expression cannot be empty.")


    no_space_expr = remove_spaces(expression)
    simplified_expr: str = simplify_signs(no_space_expr)
    tokens: list[Token] = tokenize(simplified_expr)
    postfix_tokens: list[Token] = convert_to_postfix(tokens)
    return postfix_calculator(postfix_tokens)
