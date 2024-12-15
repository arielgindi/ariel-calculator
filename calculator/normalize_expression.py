def normalize_expression(expr: str) -> str:
    """
    Normalizes '~' usage to ensure valid expressions by validating placement
    and converting '~+' or '~-3' into their normalized forms.
    Example: "~+3" becomes "~3", "~-3" becomes "3"
    Example: "~-3!" raises ValueError, "~5!" raises ValueError
    """
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
                # Example: "~5" or "~(3+1)"
                # If digit, read the number here to check if there's a factorial next to it.
                if next_char.isdigit():
                    result += '~'
                    i += 1
                    # Read the number after '~'
                    start = i
                    while i < length and (expr[i].isdigit() or expr[i] == '.'):
                        i += 1
                    number_str = expr[start:i]
                    # If next char is '!', it's invalid usage of '~' before factorial without parentheses.
                    if i < length and expr[i] == '!':
                        raise ValueError("Invalid usage of '~' before factorial without parentheses.")
                    result += number_str
                    continue
                else:
                    # next_char == '('
                    result += '~'
                    i += 1
                    continue
            elif next_char in '+-':
                print("next_char is ", next_char)
                sign = next_char
                i += 2
                # After ~+ or ~-, we must have a digit immediately
                if i >= length or not expr[i].isdigit(): # or (
                    raise ValueError(f"Invalid usage of '~{sign}': no number follows.") #  or (
                start = i
                while i < length and (expr[i].isdigit() or expr[i] == '.'):
                    i += 1
                number_str = expr[start:i]
                # If next char is '!', again invalid without parentheses
                if i < length and expr[i] == '!' and next_char != '-':
                    raise ValueError("Invalid usage of '~' before factorial without parentheses.")
                if sign == '+':
                    # "~+3" -> "~3"
                    result += '~' + number_str
                else:
                    # "~-3" -> "3"
                    result += number_str
                continue
            elif next_char == '~':
                raise ValueError("Multiple consecutive '~' operators without parentheses are not allowed.")
            else:
                raise ValueError("Invalid usage of '~' operator.")
        else:
            result += c
            i += 1
    return result
