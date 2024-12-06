from utils import simplify_signs
from tokens import tokenize
from parser import convert_to_postfix, postfix_calculator

def calculator(expression: str) -> float:
    cleaned = simplify_signs(expression)
    tok = tokenize(cleaned)
    post = convert_to_postfix(tok)
    return postfix_calculator(post)
