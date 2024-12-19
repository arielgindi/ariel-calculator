from calculator.Token import Token

def validate_tilda(tokens: list[Token]) -> None:
    """
    Validate the correct usage of the tilde (~) operator in the token sequence.

    This function ensures that:
    1. The tilde (~) operator does not appear immediately after a unary sign operator (u- or u+).
    2. Multiple consecutive tilde operators (~) are not allowed before a single number.
    """
    def is_unary_sign(t: Token) -> bool:
        return t.value in ["u-", "u+"]

    i: int = 1
    while i < len(tokens):
        if tokens[i].value == '~':
            if is_unary_sign(tokens[i - 1]):
                raise ValueError("unary sign cannot become before ~")

            i += 1
            while i < len(tokens) and tokens[i].token_type == "OPERATOR":
                if tokens[i].value == '~':
                    raise ValueError("Multiple ~ before a single number is not allowed")
                i += 1
        else:
            i += 1
