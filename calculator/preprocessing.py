from calculator.utils.remove_spaces import remove_spaces
from calculator.utils.simplify_signs import simplify_signs

def normalize_expression(expr: str) -> str:
    i = 0
    result = ""
    length = len(expr)
    while i < length:
        c = expr[i]
        if c == '~':
            if i == length - 1:
                raise ValueError("Invalid usage of '~' at end of expression.")
            next_char = expr[i+1]
            if next_char.isdigit() or next_char == '(':
                result += '~'
                i += 1
                continue
            elif next_char in '+-':
                sign = next_char
                i += 2
                if i >= length:
                    raise ValueError("Invalid usage of '~', missing number after sign.")
                if sign == '+':
                    if not expr[i].isdigit():
                        raise ValueError("Invalid usage of '~+': no number follows.")
                    start = i
                    while i < length and (expr[i].isdigit() or expr[i] == '.'):
                        i += 1
                    number_str = expr[start:i]
                    result += '~' + number_str
                    continue
                else:
                    result += '~(' + sign
                    if i >= length or not expr[i].isdigit():
                        raise ValueError("Invalid usage of '~-': no number follows.")
                    start = i
                    while i < length and (expr[i].isdigit() or expr[i] == '.'):
                        i += 1
                    number_str = expr[start:i]
                    result += number_str + ')'
                    continue
            elif next_char == '~':
                raise ValueError("Multiple consecutive '~' operators without parentheses are not allowed.")
            else:
                raise ValueError("Invalid usage of '~' operator.")
        else:
            result += c
            i += 1
    return result

def final_preprocessing(expression: str) -> str:
    no_space_expr = remove_spaces(expression)
    simplified_expr = simplify_signs(no_space_expr)
    normalized = normalize_expression(simplified_expr)
    return normalized
