
# DICT = {'a': 'alpha', 'b': 'beta', 'c': 'theta'}
L = [('a', 'alpha'), ('b', 'beta'), ('c', 'theta')]

if __name__ == '__main__':

    print(L)

    for t in L:
        exec(f'{t[0]} = "{t[1]}"')

    # FIXME a, b, c can't be accessed
    print(a)
    print(b)
    print(c)

