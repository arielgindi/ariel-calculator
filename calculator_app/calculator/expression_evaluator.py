from utils import simplify_signs
from tokens import tokenize, Token
from parser import convert_to_postfix, postfix_calculator

def calculator(expression: str) -> float:
    expression = expression.replace(" ", "")
    if not expression:
        return False
    cleaned: str = simplify_signs(expression)
    tok: list[Token] = tokenize(cleaned)
    post: list[Token] = convert_to_postfix(tok)
    return postfix_calculator(post)
