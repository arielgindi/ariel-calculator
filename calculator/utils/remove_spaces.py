def remove_spaces(expr: str) -> str:
    """
    Removes extra spaces and ensures numbers aren't separated by spaces.
    Example: "12 34 + 56" raises ValueError,
    Example: "12 + 34"    return "12+34"
    """
    expr = ' '.join(expr.split())

    for i in range(len(expr) - 2):
        if expr[i].isdigit() and expr[i + 1] == ' ' and expr[i + 2].isdigit():
            raise ValueError("Invalid spacing: numbers cannot be separated by a space")

    cleaned_expr = expr.replace(' ', '')
    if not cleaned_expr:
        raise ValueError("Expression is empty after removing spaces.")

    return cleaned_expr
