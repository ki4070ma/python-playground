
class clsA:

    def __init__(self, name):
        self.name = name

    def get(self):
        return self.name

    def set(self, name):
        self.name = name

class clsMain():

    def __init__(self):
        self.cls_a = clsA('aaa')

    a_property: clsA = property(lambda self: self.cls_a)

    get_a_lambda: clsA = lambda self: self.cls_a

    def get_a_def(self) -> clsA:
        return self.cls_a

    @property
    def a_def(self) -> clsA:
        return self.cls_a

if __name__ == '__main__':

    cls_a = clsA('a')
    print(cls_a.get())  # Type hint works

    cls_main = clsMain()
    print(cls_main.get_a_def().get())  # Type hint works
    print(cls_main.a_def.get())  # Type hint works

    print(cls_main.get_a_lambda().get()) # Type hint doesn't work
    print(cls_main.a_property.get()) # Type hint doesn't work


