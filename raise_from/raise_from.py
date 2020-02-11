
# https://docs.python.org/ja/3.8/library/exceptions.html
# https://docs.python.org/ja/3/reference/simple_stmts.html#the-raise-statement


def raise_exc():
    try:
        print(1 / 0)
    except Exception as exc:
        raise exc

def raise_from_exc():
    try:
        print(1 / 0)
    except Exception as exc:
        raise RuntimeError("Something bad happened") from exc

def raise_from_None():
    try:
        print(1 / 0)
    except Exception:
        raise RuntimeError("Something bad happened") from None


if __name__ == '__main__':
    raise_exc()
    # raise_from_exc()
    # raise_from_None()