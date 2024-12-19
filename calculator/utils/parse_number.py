def parse_number(value):
    try:
        s = str(value).strip()
        if '.' in s:
            integer_part, fractional_part = s.split('.', 1)

            if fractional_part == '' or all(c == '0' for c in fractional_part):
                return int(integer_part)
            else:
                f = float(s)
                return int(f) if f.is_integer() else f
        else:
            return int(s)

    except ValueError:
        raise ValueError(f"Cannot convert '{value}' to a number.")
