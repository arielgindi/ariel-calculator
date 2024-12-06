from operations import operator_precedence

class Token:
    VALID_TYPES = {"NUMBER", "OPERATOR"}

    def __init__(self, token_type: str, value: float | str = None):
        if token_type not in self.VALID_TYPES:
            raise ValueError("Invalid token type")
        self.token_type = token_type
        self.value = value
        self.operator_precedence = operator_precedence[value] if token_type == "OPERATOR" and value in operator_precedence else None

    def __repr__(self) -> str:
        return f"Token({self.token_type}, {self.value})"

def tokenize(expr: str) -> list[Token]:
    expr = expr.replace(" ", "")
    tokens = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c.isdigit() or c == '.':
            start = i
            i += 1
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                i += 1
            number_val = float(expr[start:i])
            tokens.append(Token("NUMBER", number_val))
            continue
        elif c in ['+', '-']:
            if not tokens or tokens[-1].token_type == "OPERATOR":
                sign = 1 if c == '+' else -1
                i += 1
                if i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                    start = i
                    i += 1
                    while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                        i += 1
                    number_val = float(expr[start:i]) * sign
                    tokens.append(Token("NUMBER", number_val))
                    continue
                else:
                    raise ValueError("Invalid unary operator usage")
            else:
                tokens.append(Token("OPERATOR", c))
                i += 1
                continue
        elif c in '*/^%$&@~!':
            tokens.append(Token("OPERATOR", c))
            i += 1
            continue
        else:
            raise ValueError("Invalid character")
    return tokens
