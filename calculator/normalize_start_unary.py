from calculator.Token import Token


def normalize_start_unary(tokens: list[Token]) -> list[Token]:
    """
    Converts unary operators ('u+' and 'u-') at the start of the expression
    into '0+' and '0-' respectively.
    """

    # if ~ is found at the first index than its first in precedence and no need to convert it to binary sign
    # for example:
    # -3! -> 0-3!
    # ~3! -> ~3!
    if tokens[0].value == '~':
        return tokens

    i: int = 0
    result_tokens: list[Token] = []



    # Handle leading unary operators
    while i < len(tokens) and tokens[i].token_type == "OPERATOR":
        operator = tokens[i].value
        if operator == 'b+':
            result_tokens.extend([Token("NUMBER", 0), Token("OPERATOR", '+')])
        elif operator == 'b-':
            result_tokens.extend([Token("NUMBER", 0), Token("OPERATOR", '-')])
        else:
            raise ValueError(f"Unexpected operator {tokens[i]} after unary sign")
        i += 1

    # Append the rest of the tokens
    result_tokens.extend(tokens[i:])
    return result_tokens
