from calculator.normalize_expression import normalize_expression
from calculator.utils.remove_spaces import remove_spaces
from calculator.utils.simplify_signs import simplify_signs


def final_preprocessing(expression: str) -> str:
    no_space_expr = remove_spaces(expression)
    # simplified_expr = simplify_signs(no_space_expr)
    # normalized = normalize_expression(no_space_expr)
    return no_space_expr
