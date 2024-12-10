def parse_number(value: int | float | str) -> int | float:
    if isinstance(value, int):
        return value

    if isinstance(value, float):
        if value.is_integer():
            return int(value)
        return value

    # since it's a string, convert it to float and return the minimal version of it
    return parse_number(float(value))