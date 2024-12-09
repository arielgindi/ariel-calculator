from operations import OPERATORS, FILTERED_OPERATORS


class Token:
    VALID_TYPES = {"NUMBER", "OPERATOR", "LPAREN", "RPAREN" }

    def __init__(self, token_type: str, value: float | str = None):
        if token_type not in self.VALID_TYPES:
            raise ValueError("Invalid token type")
        self.token_type = token_type
        self.value = value
        self.operator_precedence = (
            OPERATORS[value]['precedence']
            if token_type == "OPERATOR" and value in OPERATORS
            else None
        )

    def __repr__(self) -> str:
        return f"Token({self.token_type}, {self.value})"
def tokenize(expr: str) -> list[Token]:
    expr = expr.replace(" ", "")
    tokens = []
    i = 0
    while i < len(expr):
        c = expr[i]
        # Handle numbers
        if c.isdigit() or c == '.':
            start = i
            i += 1
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                i += 1
            number_val = float(expr[start:i])
            tokens.append(Token("NUMBER", number_val))
            continue

        elif c in '+-':
            # Check if unary plus/minus: if at start or after operator or '('
            if not tokens or tokens[-1].token_type in ("OPERATOR", "LPAREN"):
                # Unary scenario
                sign_char = c
                i += 1
                if i < len(expr):
                    next_char = expr[i]
                    if next_char.isdigit() or next_char == '.':
                        # If unary minus, insert 0 before minus to maintain correct precedence
                        if sign_char == '-':
                            tokens.append(Token("NUMBER", 0.0))
                            tokens.append(Token("OPERATOR", '-'))
                        # If unary plus, just skip the plus; no zero inserted
                        # Now read the number
                        start = i
                        i += 1
                        while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                            i += 1
                        number_val = float(expr[start:i])
                        tokens.append(Token("NUMBER", number_val))
                        continue
                    elif next_char == '(':
                        # If we have something like "-(" or "+("
                        # For unary minus, insert 0 and minus
                        if sign_char == '-':
                            tokens.append(Token("NUMBER", 0.0))
                            tokens.append(Token("OPERATOR", '-'))
                        # For unary plus, do nothing special, just continue
                        # We don't consume '(' here; let next iteration handle it
                        continue
                    else:
                        # Invalid character after unary sign
                        raise ValueError("Invalid usage of unary operator.")
                else:
                    raise ValueError("Expression ends with a unary operator.")
            else:
                # Normal binary plus/minus
                tokens.append(Token("OPERATOR", c))
                i += 1
                continue

        elif c in FILTERED_OPERATORS:
            tokens.append(Token("OPERATOR", c))
            i += 1
            continue

        elif c == '(':
            tokens.append(Token("LPAREN", '('))
            i += 1
            continue

        elif c == ')':
            tokens.append(Token("RPAREN", ')'))
            i += 1
            continue

        else:
            raise ValueError(f"Invalid character '{c}' in expression")
    return tokens