from calculator.Token import Token

def validate_tilda(tokens: list[Token]) -> None:
    """
    Validate correct usage of the '~' operator:
    1. '~' cannot directly follow a unary sign operator ('u-', 'u+', 'b-', 'b+').
    2. Consecutive '~' operators (like '~~') are not allowed.
    """

    def is_unary_sign(token: Token) -> bool:
        return token.value in ["b-", "b+", "u-", "u+"]

    for i in range(1, len(tokens)):
        if tokens[i].value == '~':
            prev = tokens[i - 1]
            if is_unary_sign(prev):
                raise ValueError("unary sign cannot come before ~")
            if prev.value == '~':
                raise ValueError("Multiple ~ before a single number is not allowed")