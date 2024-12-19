# File: ./calculator/normalize_unary.py
from calculator.Token import Token

def normalize_unary(tokens: list[Token]) -> list[Token]:
    """
    Adjust '+' and '-' operators based on context using states.
    Also handles invalid double '~' usage.
    """

    START_LIKE = 'start_like'
    OPERATOR = 'operator'
    NUMBER = 'number'

    state = START_LIKE
    result: list[Token] = []

    # Track the last operator to detect invalid "~"
    last_was_tilde = False

    for t in tokens:
        if t.token_type == "NUMBER":
            result.append(t)
            state = NUMBER
            last_was_tilde = False

        elif t.token_type == "LPAREN":
            result.append(t)
            state = START_LIKE
            last_was_tilde = False

        elif t.token_type == "RPAREN":
            result.append(t)
            state = NUMBER
            last_was_tilde = False

        elif t.token_type == "OPERATOR":
            val = t.value

            if val in ['+', '-']:
                # Convert based on state
                if state == START_LIKE:
                    new_val = 'u' + val  # u+ / u-
                    # after u+ / u-, we remain in START_LIKE (multiple unary allowed)
                    state = START_LIKE
                    last_was_tilde = False
                elif state == OPERATOR:
                    new_val = 'b' + val  # b+ / b-
                    # after b+ / b-, expecting a number, stay in OPERATOR state
                    state = OPERATOR
                    last_was_tilde = False
                else:  # state == NUMBER
                    # binary + or -
                    new_val = val
                    # after binary + or -, we are waiting for a number => OPERATOR state
                    state = OPERATOR
                    last_was_tilde = False

                result.append(Token("OPERATOR", new_val))

            elif val in ['!', '#']:
                # ! and # produce a number result
                result.append(t)
                state = NUMBER
                last_was_tilde = False

            elif val == '~':
                # Check double tilde without intervening number/parentheses
                if last_was_tilde:
                    # This means we had ~~ without a number or parentheses in between
                    # The tests require this to raise ValueError
                    raise ValueError("Multiple consecutive '~' are not allowed without parentheses or a number in between.")
                result.append(t)
                # after ~, we consider state = OPERATOR (waiting for a number/unary)
                state = OPERATOR
                last_was_tilde = True

            else:
                # Any other binary operator transitions to OPERATOR state
                result.append(t)
                state = OPERATOR
                last_was_tilde = False

        else:
            # Unexpected token type (should not happen)
            result.append(t)
            last_was_tilde = False

    return result
