def sub(a: int, b: int) -> int:
    return a - b


def sub_complex(a: int, b: int) -> int:
    if not isinstance(a, str) and not isinstance(b, str):
        if a > 0:
            if b > 0:
                if a > b:
                    return a - b
                elif a == b:
                    return 0
                else:
                    return b - a
            else:
                return a
        else:
            return b
    else:
        try:
            return sub(int(a), int(b))
        except ValueError:
            print("Caught a value error")
