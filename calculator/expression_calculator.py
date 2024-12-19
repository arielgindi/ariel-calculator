from calculator.normalize_unary import normalize_unary
from calculator.tokenize import tokenize
from calculator.Token import Token
from calculator.postfix_parser import convert_to_postfix
from calculator.postfix_calculator import postfix_calculator
from calculator.final_preprocessing import final_preprocessing
from calculator.validate_tilda import validate_tilda


def calculate_expression(expression: str) -> float | int:
    if not expression:
        raise ValueError("Expression cannot be empty.")

    normalized_expr = final_preprocessing(expression)
    tokens: list[Token] = tokenize(normalized_expr)

    unary_tokens = normalize_unary(tokens)
    validate_tilda(unary_tokens)

    postfix_tokens: list[Token] = convert_to_postfix(unary_tokens)
    return postfix_calculator(postfix_tokens)
