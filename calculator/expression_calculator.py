from calculator.tokens import tokenize, Token
from calculator.postfix_parser import convert_to_postfix
from calculator.postfix_calculator import postfix_calculator
from calculator.final_preprocessing import final_preprocessing

def calculate_expression(expression: str) -> float | int:
    if not expression:
        raise ValueError("Expression cannot be empty.")

    normalized_expr = final_preprocessing(expression)
    tokens: list[Token] = tokenize(normalized_expr)
    postfix_tokens: list[Token] = convert_to_postfix(tokens)
    return postfix_calculator(postfix_tokens)
