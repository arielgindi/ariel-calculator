from typing import List, Union
from operations import OPERATORS


class Token:
    VALID_TYPES = {"NUMBER", "OPERATOR", "LPAREN", "RPAREN"}

    def __init__(self, token_type: str, value: Union[float, str]):
        if token_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid token type: {token_type}")

        self.token_type = token_type
        self.value = value
        self.operator_precedence = (
            OPERATORS[value]['precedence']
            if token_type == "OPERATOR" and value in OPERATORS
            else None
        )

    def __repr__(self) -> str:
        return f"Token({self.token_type}, {self.value})"


def tokenize(expression: str) -> List[Token]:
    """
    Convert a mathematical expression into a list of tokens.
    Numbers, operators, parentheses, and unary signs are handled.
    """
    expr = expression.replace(" ", "")
    tokens: List[Token] = []
    length = len(expr)
    index = 0

    def is_number_char(ch: str) -> bool:
        return ch.isdigit() or ch == '.'

    def is_unary_context() -> bool:
        # Unary context if at start or after an operator or '('
        return (not tokens) or (tokens[-1].token_type in ("OPERATOR", "LPAREN"))

    all_operator_symbols = set(OPERATORS.keys())

    while index < length:
        char = expr[index]

        # Handle numbers (possibly floating point)
        if is_number_char(char):
            start = index
            index += 1
            while index < length and is_number_char(expr[index]):
                index += 1
            number_str = expr[start:index]
            tokens.append(Token("NUMBER", float(number_str)))
            continue

        # Handle operators (including unary + and -)
        elif char in all_operator_symbols:
            if char in ['+', '-']:
                # '+' or '-' might be unary if in a unary context
                if is_unary_context():
                    sign = char
                    index += 1
                    if index >= length:
                        raise ValueError("Expression ends with a unary operator.")

                    next_char = expr[index]
                    if is_number_char(next_char):
                        # Unary minus: insert 0 then '-'
                        if sign == '-':
                            tokens.append(Token("NUMBER", 0.0))
                            tokens.append(Token("OPERATOR", '-'))
                        # Unary plus: just skip it
                        start = index
                        index += 1
                        while index < length and is_number_char(expr[index]):
                            index += 1
                        number_str = expr[start:index]
                        tokens.append(Token("NUMBER", float(number_str)))
                        continue
                    elif next_char == '(':
                        # for example: "-(3+2)" means 0 - (3+2)
                        # it convert "-num" ->  "0-num"
                        if sign == '-':
                            tokens.append(Token("NUMBER", 0.0))
                            tokens.append(Token("OPERATOR", '-'))
                        # Unary plus before '(' does nothing special
                        # Don't consume '(' here; next iteration will handle it
                        continue
                    else:
                        raise ValueError("Invalid character after unary sign.")
                else:
                    # Binary '+' or '-'
                    tokens.append(Token("OPERATOR", char))
                    index += 1
                    continue
            else:
                # Other operators like *, /, ^, %, $, &, @, ~, !
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
            # Unrecognized character
            raise ValueError(f"Invalid character '{char}' in expression.")

    return tokens
