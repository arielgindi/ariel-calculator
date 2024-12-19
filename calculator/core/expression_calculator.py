from calculator.core.normalize_unary import normalize_unary
from calculator.utils.tokenize import tokenize
from calculator.core.Token import Token
from calculator.core.postfix_parser import convert_to_postfix
from calculator.core.postfix_calculator import postfix_calculator
from calculator.utils.validate_tilda import validate_tilda


def calculate_expression(expression: str) -> float | int:
    if not expression:
        raise ValueError("Expression cannot be empty.")

    tokens: list[Token] = tokenize(expression)
    unary_tokens = normalize_unary(tokens)
    validate_tilda(unary_tokens)
    postfix_tokens: list[Token] = convert_to_postfix(unary_tokens)
    return postfix_calculator(postfix_tokens)
