from calculator.Token import Token


def normalize_unary(tokens: list[Token]) -> list[Token]:
    """
    Adjusts unary '+' and '-' operators in the token list to 'u+' and 'u-'.
    Unary operators occur at the start, after another operator, or after '('.
    """

    is_prev_operator = True  # Tracks if the context expects a unary operator.

    for t in tokens:
        if t.token_type == "OPERATOR":
            if t.value in ["+", "-"] and is_prev_operator:
                t.value = f"b{t.value}"  # Convert to unary form.
            is_prev_operator = True  # Operators reset the unary context.

        elif t.token_type == "LPAREN":
            is_prev_operator = True  # '(' allows a unary operator next.

        elif t.token_type == "RPAREN":
            is_prev_operator = False  # ')' ends an expression.

        else:
            is_prev_operator = False  # Numbers or other tokens reset unary context.

    return tokens