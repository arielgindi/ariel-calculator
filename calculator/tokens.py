from calculator.operations import OPERATORS

class Token:
    VALID_TYPES: set[str] = {"NUMBER", "OPERATOR", "LPAREN", "RPAREN"}

    def __init__(self, token_type: str, value: int | float | str) -> None:
        if token_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid token type: {token_type}")

        self.token_type: str = token_type
        self.value: int | float | str = value
        self.operator_precedence: float | None = (
            OPERATORS[value]['precedence']
            if token_type == "OPERATOR" and value in OPERATORS
            else None
        )

    def __repr__(self) -> str:
        return f"Token({self.token_type}, {self.value})"

def tokenize(expression: str) -> list[Token]:
    expr: str = expression.replace(" ", "")
    tokens: list[Token] = []
    length: int = len(expr)
    index: int = 0

    def is_number_char(ch: str) -> bool:
        return ch.isdigit() or ch == '.'

    def is_unary_context() -> bool:
        return (not tokens) or (tokens[-1].token_type in ("OPERATOR", "LPAREN"))

    all_operator_symbols = set(OPERATORS.keys())

    while index < length:
        char = expr[index]

        if is_number_char(char):
            start: int = index
            index += 1
            while index < length and is_number_char(expr[index]):
                index += 1
            number_str = expr[start:index]
            if '.' in number_str:
                tokens.append(Token("NUMBER", float(number_str)))
            else:
                tokens.append(Token("NUMBER", int(number_str)))
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