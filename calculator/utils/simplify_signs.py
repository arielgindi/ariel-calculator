def simplify_signs(expr: str) -> str:
    result: str = ""
    i: int = 0
    while i < len(expr):
        c = expr[i]
        if c in '+-':
            start: int = i
            while i < len(expr) and expr[i] in '+-':
                i += 1
            seq: str = expr[start:i]
            minus_count: int = seq.count('-')
            final_sign: str = '-' if minus_count % 2 == 1 else '+'
            result += final_sign
            continue
        else:
            result += c
        i += 1
    return result
