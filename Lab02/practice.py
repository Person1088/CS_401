def is_balanced(input : str) -> bool:
    st = []

    ltr: str
    for ltr in input:
        if ltr == "(":
            st.append(ltr)

        elif ltr == ")":
            if not st:
                return False
            st.pop()
    return not st

print(is_balanced("()())"))