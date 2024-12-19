from calculator.core.Token import Token
from calculator.core.operations import OPERATORS

def convert_to_postfix(tokens: list[Token]) -> list[Token]:
    """
    Converts an infix tokenized expression to postfix notation using the Shunting Yard algorithm.
    Example: [Token("NUMBER", 3), Token("OPERATOR", "+"), Token("NUMBER", 4)] returns [Token("NUMBER", 3), Token("NUMBER", 4), Token("OPERATOR", "+")].
    Raises ValueError for mismatched parentheses or unknown operators.
    """
    if not tokens:
        raise ValueError("Cannot convert an empty token list to postfix.")

    output: list[Token] = []
    stack: list[Token] = []
    for t in tokens:
        if t.token_type == "NUMBER":
            output.append(t)
        elif t.token_type == "OPERATOR":
            if t.value not in OPERATORS:
                raise ValueError(f"Unknown operator '{t.value}'.")
            while stack and stack[-1].token_type == "OPERATOR":
                top_op = stack[-1].value
                top_precedence = OPERATORS[top_op]['precedence']
                current_precedence = OPERATORS[t.value]['precedence']
                current_assoc = OPERATORS[t.value]['associativity']

                should_pop = False
                if current_assoc == 'left' and top_precedence >= current_precedence:
                    should_pop = True
                elif current_assoc == 'right' and top_precedence > current_precedence:
                    should_pop = True

                if should_pop:
                    output.append(stack.pop())
                else:
                    break
            stack.append(t)
        elif t.token_type == "LPAREN":
            stack.append(t)
        elif t.token_type == "RPAREN":
            while stack and stack[-1].token_type != "LPAREN":
                output.append(stack.pop())
            if not stack:
                raise ValueError("Mismatched parentheses: Missing '('")
            stack.pop()

    while stack:
        top = stack.pop()
        if top.token_type in ("LPAREN", "RPAREN"):
            raise ValueError("Mismatched parentheses in expression.")
        output.append(top)

    if not output:
        raise ValueError("Conversion to postfix resulted in an empty output, invalid expression.")

    return output
