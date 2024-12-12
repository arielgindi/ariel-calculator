def parse_number(value: int | float | str) -> int | float:
    if isinstance(value, int):
        return value

    if isinstance(value, float):
        if value.is_integer():
            return int(value)
        return value

    try:
        num = float(value)
    except ValueError:
        raise ValueError(f"Cannot convert '{value}' to a number.")

    return parse_number(num)
