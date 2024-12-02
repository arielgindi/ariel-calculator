operator_precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

class Token:
    VALID_TYPES = { "NUMBER", "OPERATOR" }

    def __init__(self, token_type, value=None):
        if token_type not in self.VALID_TYPES:
            raise ValueError(f"Invalid token type: {token_type}")
        self.token_type = token_type
        self.value = value
        self.operator_precedence = (
            operator_precedence[value] if token_type == "OPERATOR" and value in operator_precedence else None
        )

    def __repr__(self):
        return f"Token({self.token_type}, {self.value})"


def evaluate_expression(num1, num2, operator):
    def divide(x, y):
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return x / y

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: divide(x, y),
    }

    if operator in operations:
        return operations[operator](num1, num2)
    else:
        raise ValueError(f"Unsupported operator: {operator}")

def tokenize(expression):
    expression = expression.replace(" ", "")
    tokens = []
    current_number = ""

    for char in expression:
        if char.isdigit() or char == ".":
            current_number += char
        else:
            if current_number:
                tokens.append(Token("NUMBER", float(current_number)))
                current_number = ""
            if char in '+-*/^%$&@~!':
                tokens.append(Token("OPERATOR", char))

    if current_number:
        tokens.append(Token('NUMBER', float(current_number)))

    return tokens


def convert_to_postfix(tokens):
    output_queue = []
    operator_stack = []

    for token in tokens:
        if token.token_type == "NUMBER":
            output_queue.append(token)
        elif token.token_type == "OPERATOR":
            while operator_stack and operator_stack[-1].operator_precedence >= token.operator_precedence:
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token.token_type == "EOF":
            pass

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return output_queue

def postfix_caculator(tokens):
    output_queue = []

    for token in tokens:
        if token.token_type == "NUMBER":
            output_queue.append(token)
        elif token.token_type == "OPERATOR":
            num2 = output_queue.pop().value
            num1 = output_queue.pop().value
            operand = token.value

            res = evaluate_expression(num1, num2, operand)
            new_number_token = Token("NUMBER", res)
            output_queue.append(new_number_token)

    return output_queue[0].value


expression_str = "3.14 + 5 * 10 - 2"
tokens = tokenize(expression_str)
print(tokens)

postfix = convert_to_postfix(tokens)
print(postfix)

result = postfix_caculator(postfix)
print(result)