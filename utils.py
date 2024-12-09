def simplify_signs(expr: str) -> str:
    expr = expr.replace(" ", "")
    result = ""
    i = 0
    while i < len(expr):
        c = expr[i]
        if c in '+-':
            start = i
            while i < len(expr) and expr[i] in '+-':
                i += 1
            seq = expr[start:i]
            minus_count = seq.count('-')
            final_sign = '-' if minus_count % 2 == 1 else '+'
            result += final_sign
            continue
        else:
            result += c
        i += 1
    return result