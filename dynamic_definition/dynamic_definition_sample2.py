
from typing import Callable

class clsA:

    def __init__(self, name):
        self.name = name

    def get(self) -> str:
        return self.name

    def set(self, name):
        self.name = name

class clsMain:

    cls_a: clsA
    cls_b: clsA
    cls_c: clsA
    cls_d: clsA

    def __init__(self):
        self.cls_a = clsA('aaa')
        self.cls_b = clsA('bbb')
        self.cls_c = clsA('ccc')
        self.__setattr__('cls_d', clsA('ddd'))
        print(vars(self))

    def get_a(self):
        return self.cls_a

    def get_b(self):
        return self.cls_b

    @property
    def get_c(self) -> clsA:
        return self.cls_c

    get_d: clsA
    get_d = property(lambda self: self.cls_d)


class double:
    def __init__(self):
        self.cls_a = 'abc'

    def return_int(self):
        return 1

    calc = lambda self, a, b: a * b
    calc_typing: Callable[[int, int], int] = lambda self, a, b: a * b

    # var: Callable[[], str]  # Type hinting doesn't work
    # var: Callable[[], str] = property(lambda self: self.cls_a)  # Type hinting doesn't work
    var: str = property(lambda self: self.cls_a)

def sample_double():
    d = double()
    # d.var = 3
    print(d.var)
    print(d.calc(1, 2))
    print(d.calc_typing(2, 3))

def main():
    cls_main = clsMain()
    for key, value in cls_main.__dict__.items():
        print(key, value)

    # print('****start')
    # import inspect
    # import pprint
    # pprint.pprint(inspect.getmembers(cls_main, predicate=inspect.ismethod))
    # pprint.pprint(inspect.getmembers(cls_main))
    # print('****end')

    print(cls_main.get_a().get())
    print(cls_main.get_b().get())
    print(cls_main.get_c.get())
    print(cls_main.get_d.get())

    print('****')


if __name__ == '__main__':
    main()
    # sample_double()
