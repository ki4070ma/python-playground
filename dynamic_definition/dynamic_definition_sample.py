
from types import MethodType
from typing import Callable

# DICT = {'a': 'alpha', 'b': 'beta', 'c': 'theta'}
L = [('a', 'alpha'), ('b', 'beta'), ('c', 'theta')]

class clsA:

    a: str
    b: str
    c: str
    get_c: Callable[[], str]

    def __init__(self):
        for t in L:
            exec(f'self.{t[0]} = "{t[1]}"')
        self.get_c = lambda : self.c

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    # https://stackoverflow.com/questions/14526652/dynamically-adding-callable-to-class-as-instance-method
    # def __get__(self, instance, owner):
    #     return MethodType(self, instance) if instance else self

if __name__ == '__main__':

    print(L)

    class_A = clsA()

    print(class_A.get_a())
    print(class_A.get_b())
    print(class_A.get_c())

