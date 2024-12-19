from calculator.core.operations import OPERATORS


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
        return f"{self.token_type}({self.value})"
