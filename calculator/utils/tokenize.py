from calculator.core.Token import Token
from calculator.core.operations import OPERATORS
from calculator.utils.parse_number import parse_number
from calculator.utils.remove_spaces import remove_spaces


def tokenize(expression: str) -> list[Token]:
    """
    Tokenizes an expression into a list of Tokens.
    Example: "3 + 4" returns [Token("NUMBER", 3), Token("OPERATOR", "+"), Token("NUMBER", 4)].
    """

    expr = remove_spaces(expression)
    tokens: list[Token] = []
    length: int = len(expr)
    index: int = 0

    all_operator_symbols = set(OPERATORS.keys())

    def is_number_char(ch: str) -> bool:
        return ch.isdigit() or ch == '.'

    while index < length:
        char = expr[index]

        if char.isspace():
            # Ignore whitespace
            index += 1
            continue

        if is_number_char(char):
            start = index
            index += 1
            while index < length and is_number_char(expr[index]):
                index += 1
            number_str = expr[start:index]

            number = parse_number(number_str)  # string to number
            tokens.append(Token("NUMBER", number))
            continue

        elif char in all_operator_symbols:
            # It's one of the known operators
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
            raise ValueError(f"Invalid character '{char}' in expression at position {index}.")

    return tokens
