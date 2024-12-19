from calculator.normalize_start_unary import normalize_start_unary
from calculator.normalize_unary import normalize_unary
from calculator.tokenize import tokenize
from calculator.Token import Token
from calculator.postfix_parser import convert_to_postfix
from calculator.postfix_calculator import postfix_calculator
from calculator.utils.remove_spaces import remove_spaces
from calculator.validate_tilda import validate_tilda


def calculate_expression(expression: str) -> float | int:
    if not expression:
        raise ValueError("Expression cannot be empty.")

    no_space_expr = remove_spaces(expression)

    tokens: list[Token] = tokenize(no_space_expr)

    unary_tokens = normalize_unary(tokens)
    validate_tilda(unary_tokens)
    normalized_start_unary = normalize_start_unary(unary_tokens)
    print(normalized_start_unary)
    postfix_tokens: list[Token] = convert_to_postfix(normalized_start_unary)
    return postfix_calculator(postfix_tokens)
