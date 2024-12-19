from calculator.Token import Token
from calculator.operations import OPERATORS
from calculator.utils.parse_number import parse_number


def tokenize(expression: str) -> list[Token]:
    """
    Tokenizes an expression into a list of Tokens.
    Example: "3 + 4" returns [Token("NUMBER", 3), Token("OPERATOR", "+"), Token("NUMBER", 4)].
    Raises ValueError for invalid characters or improper unary operator usage.
    """

    expr: str = expression.replace(" ", "")
    tokens: list[Token] = []
    length: int = len(expr)
    index: int = 0

    def is_number_char(ch: str) -> bool:
        return ch.isdigit() or ch == '.'

    def is_unary_context() -> bool:
        return (not tokens) or (
            tokens[-1].token_type in ("OPERATOR", "LPAREN")
            and tokens[-1].value != '!'
        )

    all_operator_symbols = set(OPERATORS.keys())

    while index < length:
        char = expr[index]

        if is_number_char(char):
            start: int = index
            index += 1
            while index < length and is_number_char(expr[index]):
                index += 1
            number_str = expr[start:index]
            number = parse_number(number_str)
            tokens.append(Token("NUMBER", number))
            continue

        elif char in all_operator_symbols:
            if char in ['+', '-']:
                if is_unary_context():
                    sign = char
                    index += 1
                    if index >= length:
                        raise ValueError("Expression ends with unary operator.")
                    next_char = expr[index]

                    if is_number_char(next_char):
                        if sign == '-':
                            tokens.append(Token("NUMBER", 0))
                            tokens.append(Token("OPERATOR", '-'))
                        start = index
                        index += 1
                        while index < length and is_number_char(expr[index]):
                            index += 1
                        number_str = expr[start:index]
                        if '.' in number_str:
                            tokens.append(Token("NUMBER", float(number_str)))
                        else:
                            tokens.append(Token("NUMBER", int(number_str)))
                        continue
                    elif next_char == '(':
                        if sign == '-':
                            tokens.append(Token("NUMBER", 0))
                            tokens.append(Token("OPERATOR", '-'))
                        # Let parsing continue; '(' will be handled below
                        continue
                    elif next_char == '~':
                        if sign == '-':
                            tokens.append(Token("NUMBER", 0))
                            tokens.append(Token("OPERATOR", '-'))
                        tokens.append(Token("OPERATOR", '~'))
                        index += 1
                        continue
                    else:
                        raise ValueError("Invalid character after unary sign.")
                else:
                    tokens.append(Token("OPERATOR", char))
                    index += 1
                    continue
            else:
                if char == '~':
                    if index + 1 >= length:
                        raise ValueError("Expression ends with '~'.")
                    next_char = expr[index + 1]
                    if not (is_number_char(next_char) or next_char == '('):
                        raise ValueError("Invalid usage of '~'")
                    tokens.append(Token("OPERATOR", '~'))
                    index += 1
                    continue
                tokens.append(Token("OPERATOR", char))
                index += 1
                continue

        elif char == '(':
            tokens.append(Token("LPAREN", '('))
            index += 1
            continue
        elif char == ')':
            tokens.append(Token("RPAREN", ')'))
            index += 1
            continue
        else:
            raise ValueError(f"Invalid character '{char}' in expression.")

    return tokens
