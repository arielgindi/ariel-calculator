def tokenize(st):
    st = st.replace(" ", "")
    tokens = []
    current_number = ""

    for char in st:
        if char.isdigit() or char == ".":
            current_number += char
        else:
            if current_number:
                tokens.append(current_number)
                current_number = ""
            tokens.append(char)
    if current_number:
        tokens.append(current_number)
    return tokens



st = "3.14 + 5 * 10 -- 2"
token = tokenize(st)

print(token)
