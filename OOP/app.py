from uuid import uuid4
# from moduleA import BOOTCAMPNAME
from typing import Any


# decorators =====> functioni ast ke...


class B(type):

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("call metaclass")
        return super().__call__(*args, **kwds)


class C:
    def salam(self):
        print("salam az C")


class A(C, metaclass=B):
    count = 0  # class attribute
    all_objects = []

    def __init__(self, name) -> None:
        print("init khode class")
        self.id = A.gerate_random_number()
        while self.id in A.all_objects:
            self.id = A.gerate_random_number()
        A.all_objects.append(self.id)
        self.name = name

    @classmethod
    def __new__(cls, *args, **kwargs):
        print("new khode class")
        cls.count += 1
        if cls.count > 3:
            cls.count -= 1
            return
        return super().__new__(cls)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("salam")

    def __add__(self, unyeki):
        return A(self.name + unyeki.name)

    @classmethod
    def test_class(cls):
        print(cls.count)

    @staticmethod
    def gerate_random_number():
        return uuid4()

    def get_id(self):
        print(self.id)

    def salam(self):
        super().salam()
        print("salam az A")


# a = A("a")
# b = A("b")
# c: A = a + b
# a.get_id()
# b.get_id()
# c.get_id()
# a.salam()
# print(c.name)

class F:
    def _a(self):
        pass

    def __b(self):
        pass


a = F()
# a.__b()


class D(F):
    pass


class C(D):
    pass


print("type is subclass object: ", issubclass(type, object))
print("object is subclass type: ", issubclass(object, type))
print("object is instance type: ", isinstance(object, type))
print("type is instance object: ", isinstance(type, object))
