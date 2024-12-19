from calculator.Token import Token

def normalize_unary(tokens: list[Token]) -> list[Token]:
    """
    Adjust unary and binary operators in tokens to their correct form.

    Examples:
    [-, -, 3]          => [u-, u-, 3]
    [(, -, 3, )]       => [(, u-, 3, )]
    [2, -, -, 3, !]    => [2, -, b-, 3, !]
    [(, -, -, 2, )]    => [(, u-, u-, 2, )]
    """

    START_LIKE = 'start_like'
    OPERATOR = 'operator'
    NUMBER = 'number'

    state = START_LIKE
    result: list[Token] = []

    for t in tokens:
        if t.token_type == "NUMBER":
            result.append(t)
            state = NUMBER

        elif t.token_type == "LPAREN":
            result.append(t)
            state = START_LIKE

        elif t.token_type == "RPAREN":
            result.append(t)
            state = NUMBER

        elif t.token_type == "OPERATOR":
            val = t.value

            if val in ['+', '-']:
                # Handle unary (+/-) and binary operators
                if state == START_LIKE:
                    new_val = 'u' + val
                    state = START_LIKE
                elif state == OPERATOR:
                    new_val = 'b' + val
                    state = OPERATOR
                else:  # state == NUMBER
                    new_val = val
                    state = OPERATOR

                result.append(Token("OPERATOR", new_val))

            elif val in ['!', '#']:
                # Right-associative unary operators
                result.append(t)
                state = NUMBER

            else:
                # Handle other operators (e.g., ~)
                result.append(t)
                state = OPERATOR

        else:
            # Default case for unexpected tokens
            result.append(t)

    return result
